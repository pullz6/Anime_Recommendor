from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root(): 
     return {'Hello':'World'}
 
@app.post("/description")
def get_description(description:str): 
    print(description)