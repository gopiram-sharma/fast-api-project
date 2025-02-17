from fastapi import APIRouter, HTTPException
from app.models.user import UserIn, UserOut, UserInDB
from app.db.database import db
from app.security import hash_password

router = APIRouter()

# Create a new user
@router.post("/users/", response_model=UserOut)
async def create_user(user: UserIn):
    # Hash the password before storing it
    hashed_password = hash_password(user.password)
    user_in_db = UserInDB(**user.dict(), password=hashed_password)
    
    # Insert user into the database
    result = await db.users.insert_one(user_in_db.dict())
    user_in_db.id = str(result.inserted_id)
    
    # Exclude the password from the response
    return user_in_db.copy(exclude={"password"})

# Get all users
@router.get("/users/", response_model=list[UserOut])
async def get_users():
    users_cursor = db.users.find()
    users = await users_cursor.to_list(length=None)
    
    # Exclude password field from the response
    return [UserOut(**user).dict(exclude={"password"}) for user in users]
