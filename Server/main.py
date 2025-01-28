from fastapi import FastAPI, Request

app = FastAPI()

@app.post('/')
# Any function parameter passed directly is considered as a query param ?
# To use request body we have import and use request from fastapi
async def test(request : Request):
    print((await request.body()).decode())
    return 'Hello World'