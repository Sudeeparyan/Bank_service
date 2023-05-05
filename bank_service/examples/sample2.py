from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000 )