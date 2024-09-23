from django.db.models import QuerySet

from api.models import Product
from api.services.schemas.products import (
    ProductSchema, 
    ProductListSchema,
    ProductCreateSchema,
    ProductUpdateSchema,
)


class ProductRepository:
    def filter_by(self):
        products: QuerySet[Product] = Product.objects.all()

        return ProductListSchema(products=[
            ProductSchema(
                id=product.id,
                name=product.name,
                description=product.description,
                price=product.price,
                stock=product.stock,
                created_at=product.created_at,
                updated_at=product.updated_at
            ) for product in products
        ])

    def get_by_id(self, id: int) -> ProductSchema | None:
        product: Product | None = Product.objects.filter(id=id).first()

        if product is None:
            return None

        return ProductSchema.model_validate(product)

    def create(self, product: ProductCreateSchema):
        product: Product = Product.objects.create(
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock
        )

        return ProductSchema.model_validate(product)

    def update_by_id(
        self,
        id: int,
        product: ProductUpdateSchema
    ) -> ProductSchema | None:
        updated_count = Product.objects.filter(id=id).update(
            id=id,
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock
        )

        if updated_count == 0:
            return None

        updated_product = Product.objects.get(id=id)

        return ProductSchema.model_validate(updated_product)

    def delete_by_id(self, id: int) -> bool:
        product: Product | None = Product.objects.filter(id=id).first()

        if product is None:
            return False

        try:
            product.delete()
            return True
        except Exception:
            return False
