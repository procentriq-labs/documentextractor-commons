from datetime import datetime
from enum import Enum
from pydantic import BaseModel

from .schema import SchemaCreate, SchemaResponse

class DocType(str, Enum):
    INVOICE = "invoice"
    RESUME = "resume"
    FINANCIAL_STATEMENT = "financial_statement"
    PRESENTATION = "presentation"
    CONTRACT = "contract"
    LETTER = "letter"
    EMAIL = "email"
    TIMETABLE = "timetable"
    FORM = "form"
    SURVEY = "survey"
    CERTIFICATE = "certificate"

    @classmethod
    def _missing_(cls, value):
        if(value=="none"):
            return None
        return super()._missing_(value)
    
class WorkflowCreate(BaseModel):
    name: str
    extraction_schema: SchemaCreate

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "name": "Main actor identifier",
                    "extraction_schema": {
                        "key": "main_actor",  # key should be snake case
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
                    },
                }
            ]
        }

class WorkflowUpdate(BaseModel):
    name: str | None = None
    extraction_schema: SchemaCreate | None = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "name": "New name for workflow",
                }
            ]
        }


class WorkflowResponse(BaseModel):
    id: str
    name: str
    extraction_schema: SchemaResponse
    runs: list[int]
    created_at: datetime
    updated_at: datetime | None
    created_by: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "wf_rDkgEC2aTkiNMKkFAnV8Ng",
                    "name": "Total spend extraction",
                    "extraction_schema": {
                        "id": 3,
                        "key": "total_amount",
                        "name": "Total Amount",
                        "description": "The total amount logged on the invoice",
                        "source": "data",
                        "type": "NUMBER",
                        "is_array": True,
                        "children": None,
                        "created_at": "2024-10-24T12:00:00",
                        "updated_at": None
                    },
                    "runs": [1,2,3,4],
                    "created_at": "2024-10-24T12:00:00",
                    "updated_at": None,
                    "created_by": "u_rDkgEC2aTkiNMKkFAnV8Ng",
                }
            ]
        }
