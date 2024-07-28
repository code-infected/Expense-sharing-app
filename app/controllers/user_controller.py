from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.utils.firebase import db

# Define the User model using Pydantic
class User(BaseModel):
    email: EmailStr
    name: str
    mobile_number: str

# Create a new router object for defining routes
router = APIRouter()

@router.post("/users")
async def create_user(user: User):
    """
    Create a new user in the Firestore database.
    """
    try:
        # Reference to the Firestore document using the user's email
        user_ref = db.collection('users').document(user.email)
        # Save the user data in the Firestore document
        user_ref.set(user.dict())
        return {"message": "User created successfully"}
    except Exception as e:
        # Raise an HTTP exception with a 400 status code if an error occurs
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/{email}")
async def get_user(email: str):
    """
    Retrieve a user's details from the Firestore database using their email.
    """
    try:
        # Reference to the Firestore document using the user's email
        user_ref = db.collection('users').document(email)
        user_doc = user_ref.get()
        if user_doc.exists:
            # Return the user's data if the document exists
            return user_doc.to_dict()
        else:
            # Raise an HTTP exception with a 404 status code if the user is not found
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        # Raise an HTTP exception with a 400 status code if an error occurs
        raise HTTPException(status_code=400, detail=str(e))
