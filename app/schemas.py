from pydantic import BaseModel, EmailStr, Field

class UserIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr

class UserOut(UserIn):
    id: int
