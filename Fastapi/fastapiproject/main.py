from fastapi import FastAPI
from enum import Enum



app  = FastAPI()

class availablecusines(str, Enum):
    indians = 'indians'
    americans = 'americans'
    italian = 'italian'
# @app.get("/hello/{name}")
# async def hello(name):
#     return f"welcome to fastapi tutorial {name}"

food_items = {
    'indians':['samosa','dosa'],
    'americans':['hotdog', 'piza'],
    'italian':['ravolia','pizza']
}

validcusines = food_items.keys()

couponcode = {
    1: '10%',
    2: '20%',
    3: '30%',
}

@app.get("/getcoupon/{code}")
async def get_items(code: int):
    return { 'discountamount': couponcode.get(code)}

# @app.get("/get_items/{cusine}")
# async def get_items(cusine: availablecusines):
#     return food_items.get(cusine)
