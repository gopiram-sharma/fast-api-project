from fastapi import APIRouter, HTTPException, status
from app.models.item import Item
from app.db.database import db
from bson import ObjectId
from typing import List
from functools import wraps
from app.settings import get_logger

logger = get_logger(__name__)

router = APIRouter()

collection = db["items"]

def log_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        logger.debug(f"Calling function: {func.__name__}")
        result = await func(*args, **kwargs)
        logger.debug(f"Function {func.__name__} completed")
        return result
    return wrapper

@router.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
@log_decorator
async def create_item(item: Item):
    logger.debug("Creating item: %s", item)
    item_dict = item.dict(by_alias=True)
    logger.debug(f"Item dict before adding _id: {item_dict}")
    item_dict["_id"] = str(ObjectId())
    logger.debug(f"Item dict after adding _id: {item_dict}")
    await collection.insert_one(item_dict)
    new_item = await collection.find_one({"_id": item_dict["_id"]})
    logger.info("Created item: %s", new_item)
    return Item(**new_item)

@router.get("/items/{item_id}", response_model=Item)
@log_decorator
async def read_item(item_id: str):
    logger.debug(f"Reading item with ID: {item_id}")
    try:
        object_id = ObjectId(item_id)
    except:
        logger.error(f"Invalid item ID: {item_id}")
        raise HTTPException(status_code=400, detail="Invalid item ID")
    
    logger.debug(f"Converted ObjectId: {object_id}")
    item = await collection.find_one({"_id": item_id})
    logger.info(f"Found item: {item}")
    
    if item:
        return Item(**item)
    logger.error(f"Item not found with ID: {item_id}")
    raise HTTPException(status_code=404, detail="Item not found")

@router.get("/items/", response_model=List[Item])
@log_decorator
async def get_items():
    logger.debug("Fetching all items")
    items = []
    async for item in collection.find():
        items.append(Item(**item))
    logger.info(f"Found items: {items}")
    return items
