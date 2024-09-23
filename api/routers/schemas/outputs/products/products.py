from datetime import datetime
from ninja import Schema, Field


class ProductOut(Schema):
    id: int = Field(..., description="製品ID")
    name: str = Field(..., max_length=100, description="製品名")
    description: str = Field(..., description="説明")
    price: float = Field(..., description="価格")
    stock: int = Field(..., description="在庫数")
    created_at: datetime = Field(..., description="作成日時")
    updated_at: datetime = Field(..., description="更新日時")


class ProductListOut(Schema):
    products: list[ProductOut]
