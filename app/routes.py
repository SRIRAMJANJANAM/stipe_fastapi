from fastapi import APIRouter, HTTPException
from app.schemas import Product, CartItemCreate, CartItemResponse

from app.services import *

router = APIRouter()


@router.get("/products", response_model=list[Product])
async def api_get_products():
    return await get_all_products()


@router.get("/product/{product_id}", response_model=Product)
async def api_get_product(product_id: str):
    product = await get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/cart/add", response_model=CartItemResponse)
async def api_add_to_cart(cart_item: CartItemCreate):
    cart_id = await add_to_cart(cart_item)
    return {"message": "Product added to cart successfully", "cart_id": cart_id}


from fastapi import status

@router.post("/products", response_model=dict, status_code=status.HTTP_201_CREATED)
async def api_create_product(product: Product):
    product_id = await create_product(product)
    return {"message": "Product created successfully", "product_id": product_id}
