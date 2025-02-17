from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str = Field(..., description="The name of the item")
    description: Optional[str] = Field(None, description="A description of the item")
    price: float = Field(..., description="The price of the item")
    id: Optional[str] = Field(None, alias="_id")  # Add id field, alias to _id in MongoDB
        
    def dict(self, *args, **kwargs):
        item_dict = super().dict(*args, **kwargs)
        if self.id:
            item_dict['_id'] = str(self.id)
        return item_dict
        
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example Item",
                "description": "An example item",
                "price": 19.99,
                "_id": "64b0b171f11449495797825a",  # Example ObjectId string
            }
        }

