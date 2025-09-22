from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Mount static files (your frontend)
app.mount("/static", StaticFiles(directory=Path(__file__).parent.parent / "frontend"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open(Path(__file__).parent.parent / "frontend" / "index.html", "r") as f:
        return f.read()

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI backend!"}

# Example login endpoint (you'll expand this with real authentication)
@app.post("/api/login")
async def login(username: str, password: str):
    # In a real app, you'd check credentials against a database
    if username == "admin" and password == "password":
        return {"message": "Login successful!", "token": "fake-jwt-token"}
    return {"message": "Invalid credentials"}, 401

# ... (imports) ...

@app.get("/login.html", response_class=HTMLResponse)
async def read_login():
    with open(Path(__file__).parent.parent / "frontend" / "login.html", "r") as f:
        return f.read()

# ... (other endpoints) ...

# ไว้มาปรับโค้ด API เพิ่มนะ