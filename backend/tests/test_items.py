import pytest
import httpx
from app.models.item import Item
from app.db.database import db
from fastapi import status
from bson import ObjectId
from app.settings import get_logger

logger = get_logger(__name__)
BASE_URL = "http://127.0.0.1:8000/items/"

@pytest.fixture(scope="module", autouse=True)
async def mongodb_setup_teardown():
    logger.debug("Setting up MongoDB collection for tests")
    await db["items"].delete_many({})  # Clear the collection before tests
    yield  # Run the tests
    logger.debug("Tearing down MongoDB collection after tests")
    await db["items"].delete_many({})  # Clear the collection after tests

@pytest.mark.asyncio
async def test_create_item():
    item = Item(name="Test Item", description="Test Description", price=9.99)
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=item.dict(by_alias=True))

    logger.debug(f"Response status code: {response.status_code}")
    logger.debug(f"Response content: {response.content}")

    assert response.status_code == status.HTTP_201_CREATED
    created_item = Item(**response.json())
    assert created_item.name == item.name
    assert created_item.price == item.price
    assert created_item.id is not None

@pytest.mark.asyncio
async def test_create_item_invalid_data():
    invalid_item_data = {"name": "Invalid", "price": "not a number"}
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=invalid_item_data)

    logger.debug(f"Response status code: {response.status_code}")
    logger.debug(f"Response content: {response.content}")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.asyncio
async def test_read_items():
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)

    logger.debug(f"Response status code: {response.status_code}")
    logger.debug(f"Response content: {response.content}")

    assert response.status_code == status.HTTP_200_OK
    items = [Item(**i) for i in response.json()]
    logger.debug(f"Items: {items}")

@pytest.mark.asyncio
async def test_read_item():
    item = {'name': "Test Item", 'description': "Test Description", 'price': 9.99}
    async with httpx.AsyncClient() as client:
        create_response = await client.post(BASE_URL, json=item)
        created_item = Item(**create_response.json())
        response = await client.get(f"{BASE_URL}{created_item.id}")

    logger.debug(f"Response status code: {response.status_code}")
    logger.debug(f"Response content: {response.content}")

    assert response.status_code == status.HTTP_200_OK
    retrieved_item = Item(**response.json())
    assert retrieved_item.name == item['name']
    assert retrieved_item.price == item['price']

@pytest.mark.asyncio
async def test_read_item_not_found():
    non_existent_id = ObjectId()
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}{non_existent_id}")

    logger.debug(f"Response status code: {response.status_code}")
    logger.debug(f"Response content: {response.content}")

    assert response.status_code == status.HTTP_404_NOT_FOUND