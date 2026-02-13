
from fastapi import FastAPI
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

@app.get("/")
def home():
    return {"status": "AI Core Running"}

@app.post("/mission/create")
def create_mission(mission: dict):
    r = requests.post(
        f"{SUPABASE_URL}/rest/v1/missions",
        headers=HEADERS,
        json=mission
    )
    return {"result": r.json()}

@app.get("/mission/list")
def list_missions():
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/missions",
        headers=HEADERS
    )
    return r.json()

@app.post("/agent/register")
def register_agent(agent: dict):
    r = requests.post(
        f"{SUPABASE_URL}/rest/v1/agents",
        headers=HEADERS,
        json=agent
    )
    return {"agent": r.json()}
