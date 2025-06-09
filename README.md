# E-Commerce API with FastAPI and MongoDB

## Overview
This project implements a simple e-commerce backend API using FastAPI and MongoDB. It supports:
- Fetching all products
- Fetching a product by ID
- Adding a product to cart with user address details

## Tech Stack
- FastAPI (async Python web framework)
- MongoDB (NoSQL database)
- Motor (async MongoDB driver)
- Pydantic (data validation)

## Setup Instructions

### Prerequisites
- Python 3.8+
- MongoDB (local or MongoDB Atlas cluster)
- Git

### Clone repo
```bash
git clone <repo_url>
cd ecommerce_fastapi
```

### Create virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### Setup environment variables
Create a `.env` file in the root directory and add your MongoDB connection string:

```
MONGO_DETAILS=mongodb://localhost:27017
```
Replace the value with your MongoDB Atlas connection string if using cloud.

### Run the application
```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

### API Endpoints
- GET `/products` - List all products
- GET `/product/{product_id}` - Get product details
- POST `/cart/add` - Add product to cart

Use Swagger UI at `http://127.0.0.1:8000/docs` for interactive API docs.

## Notes
- Stock updates atomically on adding product to cart.
- Basic error handling included.
- UUID-based cart IDs generated automatically.

## License
MIT
