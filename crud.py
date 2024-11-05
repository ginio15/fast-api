#Contains functions for Create, Read, Update, Delete (CRUD) operations on the database.


from sqlalchemy.orm import Session
from . import models, schemas

def create_file(db: Session, file: schemas.FileCreate, filename: str, file_type: str):
    db_file = models.File(filename=filename, file_type=file_type, user=file.user)  # Create a new file object with the provided filename, file type, and user
    db.add(db_file)  # Add the file object to the database session
    db.commit()  # Commit the changes to the database
    db.refresh(db_file)  # Refresh the file object to get the updated values from the database
    return db_file  # Return the created file object

def get_files(db: Session, user: str, file_type: str = None):
    query = db.query(models.File).filter(models.File.user == user)  # Query the database for files with the specified user
    if file_type:
        query = query.filter(models.File.file_type == file_type)  # If file_type is specified, filter the query by file type
    return query.all()  # Return all the files that match the query
