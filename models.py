#Defines the structure of the data (how files are stored in the database).



from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for the file
    filename = Column(String, unique=True, index=True, nullable=False)  # Name of the file
    file_type = Column(String, nullable=False)  # Type of the file, either 'image' or 'csv'
    upload_time = Column(DateTime(timezone=True), server_default=func.now())  # Time of file upload
    user = Column(String, index=True)  # User associated with the file
