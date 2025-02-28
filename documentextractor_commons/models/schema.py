from __future__ import annotations

from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, root_validator

class AttributeType(str, Enum):
    TEXT = "Text"
    NUMBER = "Number"
    DATE = "Date"
    TIME = "Time"
    DATETIME = "DateTime"
    ADDRESS = "Address"
    NAME = "Name"
    LINEITEM = "LineItem"

    @classmethod
    def _missing_(cls, value):
        if(value=="Other"):
            return AttributeType.TEXT
        return super()._missing_(value)

class AttributeTypeCreate(str, Enum): # Strict subset of AttributeType
    TEXT = "Text"
    NUMBER = "Number"
    DATE = "Date"
    TIME = "Time"
    DATETIME = "DateTime"

class AttributeSource(str, Enum):
    DOC_DATA = "data"
    DOC_INSIGHT = "insight"
    ERP_SAP = "sap"
    ERP_HUBSPOT = "hubspot"

class SchemaCreate(BaseModel):
    key: str | None = Field(None, pattern=r"^[A-Za-z_]*$")
    name: str | None
    description: str | None
    source: AttributeSource = AttributeSource.DOC_DATA
    type: AttributeTypeCreate | None
    is_array: bool
    children: list[SchemaCreate] | None # top-level schema needs to contain at least one child

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "key": "main_actor",  # key should be snake_case
                    "name": "Main Actor",  # this can be optional if `key` is provided
                    "description": "The person playing the main role in the script",
                    "source": "data",  # must match one of the AttributeSource enum values
                    "type": "Text",  # must match one of the AttributeType enum values
                    "is_array": False,  # boolean field
                    "children": [
                        {
                            "key": "last_name",
                            "name": "Last Name",
                            "description": "Last name of the main actor",
                            "source": "data",
                            "type": "Text",
                            "is_array": False,
                            "children": None
                        },
                        {
                            "name": "Age",
                            "description": "Age of the main actor",
                            "source": "data",
                            "type": "Number",
                            "is_array": False,
                            "children": None
                        }
                    ]
                }
            ]
        }
    
    @root_validator(pre=True)
    def validate_key_present(cls, values):
        if not values.get('name') and not values.get('key'):
            raise ValueError("Either 'name' or 'key' must be provided.")
        return values

class SchemaResponse(BaseModel):
    id: str
    key: str
    name: str
    description: str | None
    source: AttributeSource
    type: AttributeType | None
    is_array: bool
    children: list[SchemaResponse] | None
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "s_rDkgEC2aTkiNMKkFAnV8Ng",
                    "key": "letter",
                    "name": "Simple Letter",
                    "description": "A simple letter with recipient details, title, and body.",
                    "source": "data",
                    "type": None, # can remove?
                    "is_array": False,
                    "children": [
                        {
                        "id": "s_rDkgEC2aTkiNMKkFAnV8gr",
                        "key": "recipient_address",
                        "name": "Recipient Address",
                        "description": "The address the letter is sent to.",
                        "source": "data",
                        "type": "ADDRESS",
                        "is_array": False,
                        "children": [
                             {
                                "id": "atr_lnkgEC2aTkiNMKkFAnV8gr",
                                "key": "recipient_name",
                                "name": "Recipient Name",
                                "description": "The name of the letter's recipient.",
                                "source": "data",
                                "type": "TEXT",
                                "is_array": False,
                                "children": None,
                                "created_at": "2024-10-24T12:00:00",
                                "updated_at": None
                            },
                            {
                                "id": "atr_rKkgEC2aTkiNMKkFAnV8ah",
                                "key": "recipient_address",
                                "name": "Recipient Address",
                                "description": "The address of the letter's recipient.",
                                "source": "data",
                                "type": "TEXT",
                                "is_array": False,
                                "children": None,
                                "created_at": "2024-10-24T12:00:00",
                                "updated_at": None
                            },
                        ],
                        "created_at": "2024-10-24T12:00:00",
                        "updated_at": None
                        },
                        {
                        "id": "atr_rDkgEC2aTkiNMKkhadV8gr",
                        "key": "subject",
                        "name": "Subject",
                        "description": "The subject of the letter.",
                        "source": "data",
                        "type": "TEXT",
                        "is_array": False,
                        "children": None,
                        "created_at": "2024-10-24T12:00:00",
                        "updated_at": None
                        },
                        {
                        "id": "atr_ahdf3AC2aTkiNMKkhadV8gr",
                        "key": "body",
                        "name": "Body",
                        "description": "The body of the letter.",
                        "source": "user_defined",
                        "type": "TEXT",
                        "is_array": False,
                        "children": None,
                        "created_at": "2024-10-24T12:00:00",
                        "updated_at": None
                        }
                    ],
                    "created_at": "2024-10-24T12:00:00",
                    "updated_at": None
                }
            ]
        }