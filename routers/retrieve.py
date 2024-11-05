# Handles file retrieval functionality

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/files",
    tags=["files"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.FileResponse])
def read_files(
    user: str = Query(..., description="User identifier"),
    file_type: str = Query(None, description="Type of file: image or csv"),
    db: Session = Depends(get_db)
):
    files = crud.get_files(db=db, user=user, file_type=file_type)
    if not files:
        raise HTTPException(status_code=404, detail="No files found")
    return files
