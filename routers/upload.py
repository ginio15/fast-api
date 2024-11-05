# Handles file upload functionality

import os
from fastapi import APIRouter, Depends, File, UploadFile, Form, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..database import SessionLocal
from typing import List

router = APIRouter(
    prefix="/upload",
    tags=["upload"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ensure directories exist
os.makedirs("app/static/images", exist_ok=True)
os.makedirs("app/static/csvs", exist_ok=True)

@router.post("/", response_model=schemas.FileResponse)
async def upload_file(
    user: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Determine file type
    if file.content_type.startswith("image/"):
        file_type = "image"
        save_dir = "app/static/images"
    elif file.content_type == "text/csv":
        file_type = "csv"
        save_dir = "app/static/csvs"
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    # Save the file
    file_location = os.path.join(save_dir, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Create DB entry
    db_file = crud.create_file(db=db, file=schemas.FileCreate(user=user), filename=file.filename, file_type=file_type)
    return db_file
