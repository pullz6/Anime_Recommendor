import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import provide_recs


app = FastAPI()

class TextIn(BaseModel):  
     text : str
     
class recsOut(BaseModel):
     recs : str

@app.get("/")
def root(): 
     return {'Hello':'World'}
 
@app.post("/Recs",response_model=recsOut)
def predict(payload: TextIn):
    recs = provide_recs(payload.text)
    return {"Recs":recs}
