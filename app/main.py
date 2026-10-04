from fastapi import FastAPI

app = FastAPI(
    title="Taskpace API",
    description="Multi tenant SaaS backend",
    version="0.1.0",
)

@app.get("/")
async def root():
    return{
        "message":"Taskpace API is up and running"
    }