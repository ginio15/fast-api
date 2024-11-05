# FastAPI Project

## Overview
This project is a web application built using [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Features
- **High Performance**: FastAPI is built on Starlette for the web parts and Pydantic for the data parts.
- **Easy to Use**: Designed to be easy to use and learn, with great editor support.
- **Automatic Docs**: Generate OpenAPI and JSON Schema documentation automatically.
- **Dependency Injection**: Easy to use dependency injection system.

## Installation
To install the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/ginio15/fast-api.git
    cd fast-api
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the application, use the following command:
```bash
uvicorn main:app --reload
This will start the FastAPI server on http://127.0.0.1:8000.

Project Structure
main.py: The main entry point of the application.
models.py: Contains the data models used in the application.
schemas.py: Defines the data schemas for request and response models.
routers/: Contains the different route modules.
tests/: Contains the test cases for the application.
