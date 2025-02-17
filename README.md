# FastAPI Project

This is a FastAPI project to learn and demonstrates how to build a RESTful API with MongoDB as the database. The project includes endpoints for creating, reading, and listing items. It also includes logging configuration and tests to ensure the API works as expected.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [API Endpoints](#api-endpoints)
- [Logging](#logging)
- [License](#license)

## Features

- FastAPI for building the API
- MongoDB for the database
- Pydantic for data validation
- Logging configuration with file and console handlers
- Environment-based configuration using `.env` file
- Unit tests with pytest and httpx

## Requirements

- Python 3.7+
- MongoDB
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/gopiram-sharma/fastapi-project.git
    cd fastapi-project
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Install MongoDB and ensure it is running.

## Configuration

1. Create a `.env` file in the root of the project and add the following content:

    ```env
    MONGO_URI=mongodb://localhost:27017
    DB_NAME=fastapi_db
    LOG_LEVEL=INFO
    LOG_LOC="../fastapi.log"
    ```

2. Update the MongoDB connection settings in `app/db/database.py` if necessary.

## Running the Application

1. Start the FastAPI application:

    ```sh
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Running Tests

1. Ensure MongoDB is running.

2. Run the tests using pytest:

    ```sh
    pytest
    ```

## API Endpoints

### Create an Item

- **URL:** `/items/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "name": "Test Item",
        "description": "Test Description",
        "price": 9.99
    }
    ```
- **Response:**
    ```json
    {
        "name": "Test Item",
        "description": "Test Description",
        "price": 9.99,
        "_id": "60d5f9f8f8f8f8f8f8f8f8f8"
    }
    ```

### Read an Item

- **URL:** `/items/{item_id}`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "name": "Test Item",
        "description": "Test Description",
        "price": 9.99,
        "_id": "60d5f9f8f8f8f8f8f8f8f8f8"
    }
    ```

### List All Items

- **URL:** `/items/`
- **Method:** `GET`
- **Response:**
    ```json
    [
        {
            "name": "Test Item",
            "description": "Test Description",
            "price": 9.99,
            "_id": "60d5f9f8f8f8f8f8f8f8f8f8"
        }
    ]
    ```

## Logging

The application uses a custom logging configuration that writes logs to both a file and the console. The log level can be configured using the `.env` file.

- **Log File:** `../fastapi.log`
- **Log Level:** Configurable via `.env` file (`LOG_LEVEL`)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
