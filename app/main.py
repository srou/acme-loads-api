from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
import json
import os

API_KEY = os.getenv("API_KEY", "my-secret-key")  # set in Fly secrets
DATA_PATH = os.path.join(os.path.dirname(__file__), "loads.json")

app = FastAPI(title="Acme Loads API")

# --- Middleware for API key auth ---
async def verify_api_key(request: Request):
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

# --- Load mock data from JSON ---
def load_data():
    with open(DATA_PATH, "r") as f:
        return json.load(f)

@app.get("/loads")
async def get_loads(_: str = Depends(verify_api_key)):
    return load_data()

@app.get("/loads/{load_id}")
async def get_load(load_id: str, _: str = Depends(verify_api_key)):
    data = load_data()
    for load in data:
        if load["load_id"] == load_id:
            return load
    raise HTTPException(status_code=404, detail="Load not found")

@app.post("/search")
async def search_loads(filters: dict, _: str = Depends(verify_api_key)):
    data = load_data()
    results = []
    for load in data:
        match = True
        for key, val in filters.items():
            if key in load and str(val).lower() not in str(load[key]).lower():
                match = False
                break
        if match:
            results.append(load)
    return {"results": results}
