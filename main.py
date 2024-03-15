from fastapi import FastAPI

app = FastAPI()



@app.get("/{name}")
async def getUsername(name: str) :
    return f"Hello, {name}!"