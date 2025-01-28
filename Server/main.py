from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Test(BaseModel):
    name: str
    age : int
    

@app.post('/')
# Any function parameter passed directly is considered as a query param ?
# To use request body we have import and use request from fastapi
def test(t: Test):
    print(t)
    return 'Hello World'