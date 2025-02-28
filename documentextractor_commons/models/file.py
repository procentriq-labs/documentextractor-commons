from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class FileType(str, Enum):
    PDF = "application/pdf"
    HTML = "text/html"
    RTF = "application/rtf"
    DOC = "application/msword"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    PPT = "application/vnd.ms-powerpoint"
    PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"

class PendingFileResponse(BaseModel):
    id: str
    filename: str
    filetype: FileType
    size: int
    created_at: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "filep_5UxOAcqHTzeoxb3_Vvk0vA",
                    "filename": "Invoice 2024-10-24.pdf",
                    "filetype": "application/pdf",
                    "size": 43627,
                    "upload_time": "2024-10-24T18:37:41.354093",
                }
            ]
        }

class FileResponse(BaseModel):
    id: str
    filename: str
    filetype: str
    size: int
    upload_time: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "id": "filep_5UxOAcqHTzeoxb3_Vvk0vA",
                    "filename": "Foo.pdf",
                    "description": "pdf",
                    "price": 123123123,
                    "upload_time": 123123123,
                }
            ]
        }