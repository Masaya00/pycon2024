from django.urls import path

from api.routers import routers

urlpatterns = [
    path('api/', routers.api.urls),
]
