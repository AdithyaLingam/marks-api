import json
from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load data from the JSON file
def load_marks():
    with open('marks.json', 'r') as file:
        return json.load(file)

# Fetch data once at app startup
marks_data = load_marks()

@app.get("/api")
async def get_marks(name: List[str]):
    # Retrieve marks based on the names passed
    marks = [marks_data.get(n, "No marks found") for n in name]
    return {"marks": marks}
