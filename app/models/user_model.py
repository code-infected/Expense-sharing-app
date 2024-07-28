from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    email: EmailStr
    name: str
    mobile: Optional[str]
