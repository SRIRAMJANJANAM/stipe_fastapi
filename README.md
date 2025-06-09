# E-Commerce API with FastAPI and MongoDB

## Overview
This project implements a simple e-commerce backend API using FastAPI and MongoDB. It supports:
- Fetching all products
- Fetching a product by ID
- Adding a product to cart with user address details

## Tech Stack
- FastAPI 
- MongoDB 
- Motor 
- Pydantic (data validation)

## Setup Instructions

### Prerequisites
- Python 3.8
- MongoDB (local)
- Git



pip install -r requirements.txt


```
MONGO_DETAILS=mongodb://localhost:27017
```


### Run the application

**uvicorn app.main:app --reload**
```

The API will be available at: `http://127.0.0.1:8000`

### API Endpoints
- GET `/products` - List all products
- GET `/product/{product_id}` - Get product details
- POST `/cart/add` - Add product to cart
- POST `/products` - Add product 

Use Swagger UI at `http://127.0.0.1:8000/docs` for interactive API docs.



