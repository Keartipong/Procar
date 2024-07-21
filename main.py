from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    distance: int

@app.post("/data")
async def receive_data(data: Data):
    print(f"Received data: {data.distance}")
    return {"status": "success"}

if __name__ == '_main_':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)