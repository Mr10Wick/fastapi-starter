from fastapi import FastAPI, HTTPException
from app.schemas import UserIn, UserOut

app = FastAPI(title="FastAPI Starter", version="0.1.0")

DB = {}  # petit "fake DB" en mémoire

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/users", response_model=UserOut, status_code=201)
def create_user(user: UserIn):
    if user.email in DB:
        raise HTTPException(status_code=409, detail="User already exists")
    DB[user.email] = user.model_dump()
    return UserOut(id=len(DB), **DB[user.email])

@app.get("/users/{email}", response_model=UserOut)
def get_user(email: str):
    data = DB.get(email)
    if not data:
        raise HTTPException(status_code=404, detail="Not found")
    idx = list(DB.keys()).index(email) + 1
    return UserOut(id=idx, **data)
