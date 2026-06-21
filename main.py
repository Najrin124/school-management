from fastapi import FastAPI

app = FastAPI(
    title="School Management API",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "School API Running"}