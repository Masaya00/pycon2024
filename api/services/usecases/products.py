from api.datasource.products import ProductRepository
from api.services.schemas.products import (
    ProductListSchema,
    ProductSchema,
    ProductCreateSchema,
    ProductUpdateSchema,
)


def list_product_service() -> ProductListSchema:
    # 必要であればドメインサービスを呼び出す
    return ProductRepository().filter_by()


def detail_product_services(product_id: int) -> ProductSchema | None:
    # 必要であればドメインサービスを呼び出す
    return ProductRepository().get_by_id(product_id)


def create_product_services(
    product_create_in: ProductCreateSchema
) -> ProductSchema:
    # 必要であればドメインサービスを呼び出す
    return ProductRepository().create(product_create_in)


def update_product_services(
    product_id: int,
    product_update_in: ProductUpdateSchema
) -> ProductSchema | None:
    # 必要であればドメインサービスを呼び出す
    return ProductRepository().update_by_id(product_id, product_update_in)


def delete_product_services(product_id: int) -> bool:
    # 必要であればドメインサービスを呼び出す
    return ProductRepository().delete_by_id(product_id)
