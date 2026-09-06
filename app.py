import os
import sqlite3
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Secure Azure Multi-Tier Backend")

DB_PATH = os.environ.get("DB_PATH", "app_database.db")
templates = Jinja2Templates(directory="templates")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


@app.on_event("startup")
def startup_event():
    init_db()


class UserCreate(BaseModel):
    name: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/users")
def get_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, created_at FROM users")
    rows = cursor.fetchall()
    conn.close()
    users = [{"id": r[0], "name": r[1], "created_at": r[2]} for r in rows]
    return {"status": "success", "data": users}


@app.post("/api/users", status_code=201)
def add_user(user: UserCreate):
    clean_name = user.name.strip()
    if not clean_name:
        raise HTTPException(status_code=400, detail="Name is required")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (clean_name,))
    conn.commit()
    conn.close()
    return {"status": "success", "message": f"User '{clean_name}' created!"}