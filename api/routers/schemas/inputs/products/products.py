from ninja import Field, Schema


class ProductCreateIn(Schema):
    name: str = Field(..., max_length=100, description="製品名")
    description: str = Field(..., description="説明")
    price: float = Field(..., description="価格")
    stock: int = Field(..., description="在庫数")


class ProductUpdateIn(Schema):
    name: str = Field(..., max_length=100, description="製品名")
    description: str = Field(..., description="説明")
    price: float = Field(..., description="価格")
    stock: int = Field(..., description="在庫数")
