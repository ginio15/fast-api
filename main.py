
from fastapi import FastAPI
from .database import engine, Base
from .routers import upload, retrieve
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount static directories
app.mount("/static/images", StaticFiles(directory="app/static/images"), name="images")
app.mount("/static/csvs", StaticFiles(directory="app/static/csvs"), name="csvs")

# Include routers
app.include_router(upload.router)
app.include_router(retrieve.router)

# Templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_root():
    return {"message": "Welcome to the File Upload and Retrieval App"}
