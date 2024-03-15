from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class jsonIn(BaseModel) :
    a: int
    b: int

class jsonOut(BaseModel) :
    sum: int

@app.post("/adder/")
async def add(input_num: jsonIn) :
    try :
        sum = input_num.a + input_num.b
        return jsonOut(sum=sum)
    except Exception :
        raise HTTPException(status_code = 404, detail = "Wrong Input Detected")