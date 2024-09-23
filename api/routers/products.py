from ninja import Router

from api.routers.schemas.inputs.products.products import (
    ProductCreateIn,
    ProductUpdateIn
)
from api.routers.schemas.outputs.products.products import (
    ProductOut,
    ProductListOut
)
from api.routers.schemas.outputs.common.error import ValidationErrorResponse

from api.services.schemas.products import (
    ProductListSchema,
    ProductSchema,
    ProductCreateSchema,
    ProductUpdateSchema,
)
from api.services.usecases.products import (
    list_product_service,
    detail_product_services,
    create_product_services,
    update_product_services,
    delete_product_services,
)

router: Router = Router()


# 一覧
@router.get(
    "",
    description="製品一覧を取得する",
    response={200: ProductListOut, 422: ValidationErrorResponse}
)
def list_product(
    request
) -> ProductListOut:

    products: ProductListSchema = list_product_service()

    return ProductListOut(products=products.products)


# 詳細
@router.get(
    "/{product_id}",
    description="指定されたidの製品詳細を取得する",
    response={
        200: ProductOut,
        404: None, 
        422: ValidationErrorResponse
    }
)
def detail_products(
    request,
    product_id: int
) -> ProductOut:

    product: ProductSchema | None = detail_product_services(product_id)

    if product is None:
        return 404, None

    return ProductOut(
        id=product.id,
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
        created_at=product.created_at,
        updated_at=product.updated_at
    )


# 登録
@router.post(
    "",
    description="製品を登録する",
    response={200: ProductOut, 422: ValidationErrorResponse}
)
def create_products(
    request,
    product_create_in: ProductCreateIn
) -> ProductOut:

    product: ProductSchema = create_product_services(
        product_create_in=ProductCreateSchema(**product_create_in.dict())
    )
    return ProductOut(
        id=product.id,
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
        created_at=product.created_at,
        updated_at=product.updated_at
    )


# 更新
@router.put(
    "/{product_id}",
    description="指定されたidの製品を更新する",
    response={
        200: ProductOut, 
        404: None, 
        422: ValidationErrorResponse
    }
)
def update_products(
    request,
    product_id: int,
    product_update_in: ProductUpdateIn,
) -> ProductOut:

    product: ProductSchema | None = update_product_services(
        product_id,
        product_update_in=ProductUpdateSchema(**product_update_in.dict())
    )

    if product is None:
        return 404, None

    return ProductOut(
        id=product.id,
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
        created_at=product.created_at,
        updated_at=product.updated_at
    )


# 削除
@router.delete(
    "/{product_id}",
    description="指定されたidの製品を削除する",
    response={204: None, 404: None, 422: ValidationErrorResponse}
)
def delete_product(
    request,
    product_id: int
) -> None:

    result: bool = delete_product_services(product_id)

    if not result:
        return 404, None

    return 204, None
