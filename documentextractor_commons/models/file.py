from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from uuid import UUID

class FileType(str, Enum):
    PDF = "application/pdf"
    HTML = "text/html"
    RTF = "application/rtf"
    DOC = "application/msword"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    PPT = "application/vnd.ms-powerpoint"
    PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"

class FileResponse(BaseModel):
    id: UUID
    filename: str
    filetype: FileType
    size: int
    upload_time: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "f73d464e-b8fd-40b0-9f13-44d476af4c91",
                    "filename": "Invoice 2024-10-24.pdf",
                    "filetype": "application/pdf",
                    "size": 43627,
                    "upload_time": "2024-10-24T18:37:41.354093",
                }
            ]
        }