from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ProductSchema(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductListSchema(BaseModel):
    products: list[ProductSchema]


class ProductCreateSchema(BaseModel):
    name: str
    description: str
    price: float
    stock: int


class ProductUpdateSchema(BaseModel):
    name: str
    description: str
    price: float
    stock: int
