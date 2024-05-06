class ExternalDocs:
    def __init__(self, description=None, url=None):
        self.description = description
        self.url = url


class Info:
    def __init__(self, title, description, version, terms_of_service=None, contact=None, license=None,
                 external_docs=None):
        self.title = title
        self.description = description
        self.version = version
        self.terms_of_service = terms_of_service
        self.contact = contact
        self.license = license
        self.external_docs = external_docs


class Server:
    def __init__(self, url=None, description=None, variables=None):
        self.url = url
        self.description = description
        self.variables = variables


class Tag:
    def __init__(self, name, description, external_docs=None):
        self.name = name
        self.description = description
        self.external_docs = external_docs


class Path:
    def __init__(self, url=None, summary=None, description=None, operations=None, parameters=None, extensions=None):
        self.url = url
        self.summary = summary
        self.description = description
        self.operations = operations
        self.parameters = parameters
        self.extensions = extensions


class Operation:
    def __init__(self, summary, description, operation_id, request_body=None, responses=None, parameters=None,
                 security=None):
        self.summary = summary
        self.description = description
        self.operation_id = operation_id
        self.request_body = request_body
        self.responses = responses
        self.parameters = parameters
        self.security = security


class RequestBody:
    def __init__(self, description, content, required=None):
        self.description = description
        self.content = content
        self.required = required


class Response:
    def __init__(self, description, content):
        self.description = description
        self.content = content


class Parameter:
    def __init__(self, name, in_, description, required, schema_data, explode=None):
        self.name = name
        self.in_ = in_
        self.description = description
        self.required = required
        self.schema = Schema(**schema_data) if schema_data else None
        self.explode = explode


class Schema:
    def __init__(self, type_, properties=None, required=None, example=None, xml=None, default=None, enum=None):
        self.type_ = type_
        self.properties = properties
        self.required = required
        self.example = example
        self.xml = xml
        self.default = default
        self.enum = enum


class Components:
    def __init__(self, schemas=None, request_bodies=None, security_schemes=None):
        self.schemas = schemas
        self.request_bodies = request_bodies
        self.security_schemes = security_schemes


class SecurityScheme:
    def __init__(self, type_, flows=None, name=None, in_=None):
        self.type_ = type_
        self.flows = flows
        self.name = name
        self.in_ = in_




class OAuth2Flow:
    def __init__(self, authorization_url, scopes):
        self.authorization_url = authorization_url
        self.scopes = scopes


class Property:
    def __init__(self, name, **kwargs):
        self.name = name
        self.type = kwargs.get('type')
        self.format = kwargs.get('format')
        self.example = kwargs.get('example')
        self.description = kwargs.get('description')
        self.default = kwargs.get('default')
        self.nullable = kwargs.get('nullable')
        self.read_only = kwargs.get('read_only')
        self.write_only = kwargs.get('write_only')
        self.deprecated = kwargs.get('deprecated')
        self.extensions = kwargs.get('extensions')

class RequestBody:
    def __init__(self, name, description=None, content=None):
        self.name = name
        self.description = description
        self.content = content

class Property:
    def __init__(self, name: str, schema):
        self.name = name
        self.schema = schema

