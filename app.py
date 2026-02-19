from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI(title="User Account & Notes API")

# In-memory storage
users_db = {}  # {user_id: {"username": str, "notes": []}}
username_map = {} # {username: user_id}

class UserCreate(BaseModel):
    username: str

class NoteCreate(BaseModel):
    content: str

@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_account(user_in: UserCreate):
    # User Story: If username already exists -> return 409
    if user_in.username in username_map:
        raise HTTPException(status_code=409, detail="Username already exists")
    
    # User Story: Create an account with a username
    user_id = str(uuid.uuid4())
    users_db[user_id] = {"id": user_id, "username": user_in.username, "notes": []}
    username_map[user_in.username] = user_id
    return users_db[user_id]

@app.get("/users/{user_id}")
def get_user(user_id: str):
    # User Story: Retrieve account by id
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.post("/users/{user_id}/notes/")
def add_note(user_id: str, note: NoteCreate):
    # User Story: Add text notes
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id]["notes"].append(note.content)
    return {"message": "Note added successfully"}

@app.get("/users/{user_id}/notes/")
def read_notes(user_id: str):
    # User Story: Read my text notes
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"notes": users_db[user_id]["notes"]}
