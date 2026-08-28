from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name: str
    description: str
    price: float
    quantity: int

    # def __init__(self, id:int, name:str, description: str, price: str, quantity: int):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity

    #since we have imported pydantic, the constructor is created by default by pydantic