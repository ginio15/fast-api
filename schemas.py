#Defines how data is validated and what data is sent or received by the API.

from datetime import datetime
from pydantic import BaseModel

class FileCreate(BaseModel):
    user: str  # User identifier

class FileResponse(BaseModel):
    id: int  # File identifier
    filename: str  # File name
    file_type: str  # File type
    upload_time: datetime  # Time of file upload
    user: str  # User identifier

    class Config:           #allows the Pydantic model to read data from, and create models based on, ORM objects
        orm_mode = True
