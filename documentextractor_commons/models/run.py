from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Dict, Any

class RunStatus(str, Enum):
    DRAFT = "draft"
    WAITING = "waiting"
    RUNNING = "running"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    FAILED = "failed"

class RunResultResponseFormat(str, Enum):
    JSON = "json"
    CSV = "csv"
    EXCEL = "excel"

class FileExtractionResult(BaseModel):
    file_id: str
    file_name: str
    data: Dict[str, Any] | None

class RunResult(BaseModel):
    results: list[FileExtractionResult]
    errors: list[str]

class RunCreate(BaseModel):
    pending_file_ids: list[str]

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "pending_file_ids": [
                        "filep_-A5BTaGVQxe82njKX_GDHA",
                        "filep_SjrJeycYSXeoimFTa1dp5w",
                    ],
                }
            ]
        }

class RunResponse(BaseModel):
    run_num: int
    workflow_id: str
    file_ids: list[str]
    status: RunStatus
    results: RunResult | None
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "examples": [
                {
                    "run_num": 1,
                    "workflow_id": "wf_rDkgEC2aTkiNMKkFAnV8Ng",
                    "file_ids": [
                        "file_5UxOAcqHTzeoxb3_Vvk0vA"
                    ],
                    "status": RunStatus.DRAFT,
                    "results": None,
                    "created_at": "2024-10-24T18:37:41.354093",
                    "updated_at": None
                }
            ]
        }