from fastapi import FastAPI
from app.routers import items
from app.settings import get_logger

logger = get_logger(__name__)
app = FastAPI()

app.include_router(items.router)

logger.info("FastAPI application started")