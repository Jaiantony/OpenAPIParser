import json
import traceback
import yaml
import schema_class
from enum_class import Schema, DataType
from typing import List, Dict, Union


class SchemaParser:
    """Parser Class which is being used to parse the OPENAPI"""
    def __init__(self, schema_file):
        self.schema = self.load_schema(schema_file)
        self.attribute_data = {}

    def parse_data(self):
        """Parse various details from the schema"""
        self.parse_version()
        self.parse_information_details()
        self.parse_server_details()
        self.parse_external_doc_details()
        self.parse_tag_details()
        self.parse_path_details()
        self.parse_components_details()
        return self.attribute_data

    def load_schema(self, schema_file):
        """ Load OPENAPI schema from a local file"""
        try:
            with open(schema_file, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            raise ValueError("Error loading schema file {}: {}".format(schema_file, str(e)))

    def parse_version(self):
        """ Parse Version from the JSON"""
        # cleansing the version form the schema
        try:
            version = self.schema['openapi']
            self.attribute_data['version'] = version
        except KeyError:
            print(f"Exception in parse_information_details - Openapi Version Not defined")

        return self.attribute_data

    def parse_information_details(self):
        """ Parse Info Details from the JSON"""

        try:
            # cleansing the info data
            info_data = self.schema.get('info', {})
            info = schema_class.Info(
                title=info_data.get('title'),
                description=info_data.get('description'),
                version=info_data.get('version'),
                terms_of_service=info_data.get('termsOfService'),
                contact=info_data.get('contact'),
                license=info_data.get('license'),
                external_docs=info_data.get('externalDocs')
            )
            self.attribute_data['info'] = info.__dict__
        except Exception as e:
            print(f"Exception in parse_information_details -{str(e)} ")
        return self.attribute_data

    def parse_server_details(self):
        """Parse Server Details from the JSON"""
        try:
            servers_data = self.schema.get('servers', [])
            servers_list = []
            for server_data in servers_data:
                server_dict = {'url': server_data.get('url'),
                               'description': server_data.get('description'),
                               'variables': server_data.get('variables')}
                servers_list.append({k: v for k, v in server_dict.items() if v is not None})
            self.attribute_data['servers'] = servers_list

        except Exception as e:
            print(f"Exception in parse_server_details -{str(e)} ")
        return self.attribute_data

    def parse_external_doc_details(self):
        """Parse externalDoc Details from the JSON"""

        try:
            externalDocs_data = self.schema.get('externalDocs', [])
            if externalDocs_data:
                externalDoc = schema_class.ExternalDocs(description=externalDocs_data.get('description'),
                                                        url=externalDocs_data.get('url'))

                self.attribute_data['externalDocs'] = externalDoc.__dict__


        except Exception as e:
            print(f"Exception in parse_external_doc_details -{str(e)} ")
        return self.attribute_data

    def parse_tag_details(self):
        """Parse Tag Details from the JSON"""

        try:
            tag_data = self.schema.get('tags', [])
            tags_list = []
            for tag_data in tag_data:
                tag_object = schema_class.Tag(
                    name=tag_data.get('name'),
                    description=tag_data.get('description'),
                    external_docs=tag_data.get('externalDocs')
                )
                tags_list.append({k: v for k, v in tag_object.__dict__.items() if v is not None})

            self.attribute_data['tags'] = tags_list

        except Exception as e:
            print(f"Exception in parse_tag_details -{str(e)} ")
        return self.attribute_data

    def parse_path_details(self):

        """Parse Path Details from the JSON"""

        try:
            paths_data = self.schema.get('paths')
            for path_url, path_details in paths_data.items():
                operations = []
                parameters = None
                url = path_url

                for operation_method, operation_info in path_details.items():
                    # Parse operation details
                    tags = operation_info.get('tags', [])
                    summary = operation_info.get('summary', None)
                    description = operation_info.get('description', None)
                    operation_id = operation_info.get('operationId', None)
                    request_body = operation_info.get('requestBody', None)
                    responses = operation_info.get('responses', {})
                    security = operation_info.get('security', [])
                    # Parse parameters if available
                    parameters_data = operation_info.get('parameters', [])
                    if parameters_data:
                        parameters = []
                        for parameter in parameters_data:
                            parameters.append({
                                'name': parameter['name'],
                                'in': parameter['in'],
                                'description': parameter.get('description', None),
                                'required': parameter.get('required', False),
                                'schema': parameter.get('schema', {})
                            })
                    # Construct operation object
                    operation = {
                        'method': operation_method,
                        'tags': tags,
                        'summary': summary,
                        'description': description,
                        'operation_id': operation_id,
                        'request_body': request_body,
                        'responses': responses,
                        'security': security,
                        'parameters': parameters
                    }
                    operations.append(operation)

                # Create Path object and add to paths list
                path = schema_class.Path(url=url, summary=None, description=None, operations=operations,
                                         parameters=parameters,
                                         extensions=None)
                self.attribute_data['paths'] = path.__dict__
        except Exception as e:
            print(f"Exception in parse_tag_details -{str(e)} ")
        return self.attribute_data

    def parse_components_details(self):
        """Parser the components details from the JSON"""
        try:
            parameters = {}
            if 'schemas' in self.schema['components']:
                for name, prop_data in self.schema['components']['schemas'].items():
                    prop_schema = {'name': name, 'schema': {}}
                    for prop_name, prop_info in prop_data['properties'].items():
                        schema = Schema(type=prop_info.get('type', ''))
                        prop_schema['schema'][prop_name] = {
                            'name': prop_name,
                            'type': prop_info.get('type', ''),
                            'format': prop_info.get('format', ''),
                            'description': prop_info.get('description', ''),
                            'example': prop_info.get('example', ''),
                            'required': prop_name in prop_data.get('required', []),
                            'min': prop_data.get('min', None) if 'min' in prop_data else None,
                            'max': prop_data.get('max', None) if 'max' in prop_data else None
                        }
                    parameters[name] = prop_schema
                self.attribute_data['schemas'] = parameters
        except Exception as e:
            print(f"Exception in parse_components_details - {str(e)} ")
        return self.attribute_data


schema_obj = SchemaParser('v3.1_example.yml')
data = schema_obj.parse_data()
# data=json.dumps(data)
print(data)





