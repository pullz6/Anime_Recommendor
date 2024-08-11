import uvicorn
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from app.model.model import provide_recs


app = FastAPI()

class TextIn(BaseModel):  
     text : str

@app.get("/")
async def root(): 
     return {'Ready for Recs'}
 
@app.post("/predict")
def predict(req:TextIn):
    recs = provide_recs(req.text)
    print(recs)
    return {"Recs":recs}