from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
newdb : Dict[int, str] = {}

class CRUD(BaseModel) :
    content : str

@app.post('/crud/')
def create(notepad : CRUD) :
    current_notepad = len(newdb) + 1
    newdb[current_notepad] = notepad.content
    return {"notepad" : current_notepad, "content" : notepad.content}
#만들기

@app.get('/crud/{current_notepad}')
def read(current_notepad : int) :
    if current_notepad not in newdb :
        raise HTTPException(status_code = 404, detail = "Content Does Not Exist!")
    else :
        return {"notepad" : current_notepad, "content" : newdb[current_notepad]}
#읽기

@app.put("/crud/{current_notepad}")
def update(current_notepad : int, notepad : CRUD) :
    if current_notepad not in newdb :
        raise HTTPException(status_code = 404, detail = "Content Does Not Exist!")
    newdb[current_notepad] = notepad.content
    return {"notepad" : current_notepad, "content" : notepad.content}
#수정

@app.delete("/crud/{current_notepad}")
def delete(current_notepad : int) :
    if current_notepad not in newdb :
        raise HTTPException(status_code = 404, detail = "Content Does Not Exist!")
    del newdb[current_notepad]
    return {"alert" : "Notepad Deleted"}
#삭제