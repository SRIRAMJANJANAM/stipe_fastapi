from typing import List, Optional
from app.models import product_collection, cart_collection
from app.schemas import Product, CartItemCreate, CartItemInDB
from fastapi import HTTPException
from datetime import datetime
import uuid


async def get_all_products() -> List[Product]:
    products_cursor = product_collection.find({})
    products = []
    async for product in products_cursor:
        product["_id"] = str(product["_id"])
        products.append(Product(**product))
    return products


async def get_product_by_id(product_id: str) -> Optional[Product]:
    product = await product_collection.find_one({"_id": product_id})
    if product:
        product["_id"] = str(product["_id"])
        return Product(**product)
    return None


async def add_to_cart(cart_item: CartItemCreate) -> str:
    product = await product_collection.find_one({"_id": cart_item.product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if cart_item.size not in product["sizes"]:
        raise HTTPException(status_code=400, detail="Selected size not available")
    stock = product["stock"].get(cart_item.size, 0)
    if cart_item.quantity > stock:
        raise HTTPException(status_code=400, detail="Insufficient stock for selected size")
    update_result = await product_collection.update_one(
        {"_id": cart_item.product_id, f"stock.{cart_item.size}": {"$gte": cart_item.quantity}},
        {"$inc": {f"stock.{cart_item.size}": -cart_item.quantity}},
    )
    if update_result.modified_count == 0:
        raise HTTPException(status_code=400, detail="Failed to update stock, insufficient quantity")
    cart_id = "CART" + uuid.uuid4().hex[:8].upper()
    cart_data = {
        "_id": cart_id,
        "product_id": cart_item.product_id,
        "size": cart_item.size,
        "quantity": cart_item.quantity,
        "user": cart_item.user.dict(),
        "created_at": datetime.utcnow(),
    }
    await cart_collection.insert_one(cart_data)

    return cart_id


from app.models import product_collection
from app.schemas import Product
from fastapi import HTTPException

async def create_product(product: Product) -> str:
    existing = await product_collection.find_one({"_id": product.product_id})
    if existing:
        raise HTTPException(status_code=400, detail="Product with this ID already exists")
    product_doc = product.dict(by_alias=True)
    await product_collection.insert_one(product_doc)
    return product.product_id