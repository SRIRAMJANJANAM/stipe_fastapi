from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional
from datetime import datetime


class ProductStock(BaseModel):
    S: int
    M: int
    L: int
    XL: int


class Product(BaseModel):
    product_id: str = Field(..., alias="_id")
    name: str
    description: str
    price: int
    sizes: List[str]
    stock: Dict[str, int]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "P001",
                "name": "T-shirt",
                "description": "Cotton T-shirt",
                "price": 499,
                "sizes": ["S", "M", "L", "XL"],
                "stock": {"S": 5, "M": 10, "L": 3, "XL": 0},
            }
        }


class Address(BaseModel):
    line1: str
    city: str
    pincode: str
    state: str


class User(BaseModel):
    name: str
    email: EmailStr
    address: Address


class CartItemCreate(BaseModel):
    product_id: str
    size: str
    quantity: int
    user: User


class CartItemResponse(BaseModel):
    message: str
    cart_id: str


class CartItemInDB(BaseModel):
    product_id: str
    size: str
    quantity: int
    user: User
    created_at: datetime
