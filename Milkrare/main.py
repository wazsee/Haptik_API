from pickletools import string1
from urllib import response
from fastapi import FastAPI
from pydantic import BaseModel
from factory import connector1
import uvicorn
import pandas as pd

api = FastAPI()
class cattlemilkingdays(BaseModel):
    Phone_Number : int


@api.get('/api/')
async def hello_home():
    return "Welcome to the feed API!"
    
@api.post('/api/Haptik')
async def cattlemilkingdays(request:cattlemilkingdays):
    response_json = connector1.milking(request.dict())
    return response_json
if __name__ == '__main__':
    uvicorn.run(api,host='127.0.0.1',port=8000)

#server = uvicorn.run(api)
