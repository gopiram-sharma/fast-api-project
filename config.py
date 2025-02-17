import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/dbname")
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"
