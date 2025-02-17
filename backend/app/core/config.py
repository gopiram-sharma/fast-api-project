# import os
# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables from .env file

# class Settings:
#     PROJECT_NAME: str = "FastAPI MongoDB App"
#     MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
#     DB_NAME: str = os.getenv("DB_NAME", "my_database")  # Add the database name here

# settings = Settings()

from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "myapp_db"

    class Config:
        env_file = ".env"

settings = Settings()

