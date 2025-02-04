from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Optional


class CloudEventSpecVersion:
    ''' Exposes all supported versions of the Cloud Event Specification '''

    v1_0: str = "1.0"
    ''' Gets the version '1.0' of the Cloud Event Specification '''


@dataclass
class CloudEvent:
    '''
    Represents a Cloud Event.

    Attributes:
        id (str): A string that uniquely identifies the cloud event in the scope of its source.
        specversion (str): The version of the CloudEvents specification which the event uses. Defaults to '1.0'.
        time (Optional[datetime]): The date and time at which the event has been produced.
        source (str): The cloud event's source.
        type (str): The cloud event's type.
        subject (Optional[str]): A value that describes the subject of the event in the context of the event producer.
        datacontenttype (Optional[str]): The cloud event's data content type. Defaults to 'application/json'.
        dataschema (Optional[str]): An URI that references the versioned schema of the event's data.
        data (Optional[Any]): The event's data, if any. Only used if the event has been formatted using the structured mode.
        data_base64 (Optional[str]): The event's binary data, encoded in base 64. Used if the event has been formatted using the binary mode.
        **extensions: Keyword arguments representing extension attributes.
    '''

    id: str
    ''' Gets/sets string that uniquely identifies the cloud event in the scope of its source. '''

    source: str
    ''' Gets/sets the cloud event's source. Must be an absolute URI. '''

    type: str
    ''' Gets/sets the cloud event's source. Should be a reverse DNS domain name, which must only contain lowercase alphanumeric, '-' and '.' characters. '''

    specversion: str = '1.0'  # Default value for specversion
    ''' Gets/sets the version of the CloudEvents specification which the event uses. Defaults to '1.0'. '''

    sequencetype: Optional[str] = None
    ''' Gets/sets the type of the sequence. '''

    sequence: Optional[int] = None
    ''' Gets/sets the sequence of the event. '''

    time: Optional[datetime] = None
    ''' Gets/sets the date and time at which the event has been produced. '''

    subject: Optional[str] = None
    ''' Gets/sets value that describes the subject of the event in the context of the event producer. '''

    datacontenttype: Optional[str] = 'application/json'  # Default value for datacontenttype
    ''' Gets/sets the cloud event's data content type. Defaults to 'application/json'. '''

    dataschema: Optional[str] = None
    ''' Gets/sets an URI, if any, that references the versioned schema of the event's data. '''

    data: Optional[Any] = None
    ''' Gets/sets the event's data, if any. Only used if the event has been formatted using the structured mode. '''

    data_base64: Optional[str] = None
    ''' Gets/sets the event's binary data, encoded in base 64. Used if the event has been formatted using the binary mode. '''

    extensions: Dict[str, Any] = field(default_factory=dict)  # Store extensions in a dict
    ''' Gets/sets a mapping containing the event's extension attributes. '''

    def __post_init__(self, *args, **kwargs):
        # Capture any additional keyword arguments as extension attributes
        for key, value in kwargs.items():
            # only add them if they are not already defined fields
            if key not in self.__dataclass_fields__:
                self.extensions[key] = value

    def __getattr__(self, name):
        # Allow access to extensions as attributes
        if name in self.extensions:
            return self.extensions[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        # Allow setting of extensions as attributes if it is an extension or not a predefined field.
        if name in self.extensions or name not in self.__dataclass_fields__:
            self.extensions[name] = value
        else:
            super().__setattr__(name, value)  # Use default setting for standard attributes

    def get_attribute(self, name: str) -> Optional[Any]:
        ''' Gets the value of the attribute with the specified name, if any '''
        if not name:
            raise ValueError("Attribute name cannot be empty or None.")
        return getattr(self, name, None)  # Use getattr to check both standard and extension attributes
