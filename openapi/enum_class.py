from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Union


class DataType(Enum):
    NULL = 'null'
    INTEGER = 'integer'
    NUMBER = 'number'
    STRING = 'string'
    BOOLEAN = 'boolean'
    ARRAY = 'array'
    OBJECT = 'object'
    ONE_OF = 'oneOf'
    ANY_OF = 'anyOf'


class IntegerFormat(Enum):
    INT32 = 'int32'
    INT64 = 'int64'


class StringFormat(Enum):
    DATE_TIME = 'date-time'


class Property:
    def __init__(self, name: str, schema):
        self.name = name
        self.schema = schema


@dataclass
class Schema:
    def __init__(self, **kwargs):
        self.type = kwargs.get('type', DataType.OBJECT)
        self.title = kwargs.get('title', None)
        self.enum = kwargs.get('enum', [])
        self.example = kwargs.get('example', None)
        self.description = kwargs.get('description', None)
        self.default = kwargs.get('default', None)
        self.nullable = kwargs.get('nullable', False)
        self.read_only = kwargs.get('read_only', False)
        self.write_only = kwargs.get('write_only', False)
        self.deprecated = kwargs.get('deprecated', False)
        self.extensions = kwargs.get('extensions', {})
        self.max_properties = kwargs.get('max_properties', None)
        self.min_properties = kwargs.get('min_properties', None)
        self.required = kwargs.get('required', [])
        self.properties = kwargs.get('properties', [])

    def __str__(self) -> str:
        return self.description


class Integer(Schema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiple_of = kwargs.get('multiple_of', None)
        self.maximum = kwargs.get('maximum', None)
        self.exclusive_maximum = kwargs.get('exclusive_maximum', None)
        self.minimum = kwargs.get('minimum', None)
        self.exclusive_minimum = kwargs.get('exclusive_minimum', None)
        self.format = kwargs.get('format', None)


class String(Schema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_length = kwargs.get('max_length', None)
        self.min_length = kwargs.get('min_length', None)
        self.pattern = kwargs.get('pattern', None)
        self.format = kwargs.get('format', None)


class Boolean(Schema):
    pass


class Array(Schema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = kwargs.get('items', None)