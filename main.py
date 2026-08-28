from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
import database_models 
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind = engine)

@app.get("/")
def greet():
    return("Welcome to Home")

products =  [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(database_models.Product).count()

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

    db.commit()  #we have to do this manually because we had put autocommit as false

    """initially the products are of type defined by pydantic, we need to convert it to sqlachemy type
    to get the data stored. So we use database_model.Product(product) to convert from pydantic to sqlachemy
    and to get data, we use model_dump. 
    Model dump gives all data in dictionary format, so we need to unpack it, for that we use ** at start"""

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):    #dependency injection
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int,  db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first() 
    for product in products:
        if product.id == id:
            return product

    return "product not found"


@app.post("/products")
def add_product(product: Product, db : Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit() 
    return product

@app.put("/products/{id}")
def update_product(id: int, product : Product,  db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first() 

    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()

    else:   
        return "No product found"


@app.delete("/products")
def delete_product(id: int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first() 

    if db_product:
        db.delete(db_product)
        db.commit()
    else:  
        return "Not found"