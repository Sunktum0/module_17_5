
from fastapi import FastAPI
from routers import task, user

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router, prefix="/task", tags=["tasks"])
app.include_router(user.router, prefix="/user", tags=["users"])

if __name__ == "__main__":
    import uvicorn
    from models import Base
    from backend.db import engine

    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="127.0.0.1", port=8000)