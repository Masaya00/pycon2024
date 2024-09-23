from ninja import NinjaAPI

from api.routers.orders import router as orders_router
from api.routers.products import router as products_router

api: NinjaAPI = NinjaAPI(
    title="Ninja API",
)

api.add_router("/products", products_router, tags=["products"])
api.add_router("/orders", orders_router, tags=["orders"])
