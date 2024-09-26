from django.conf import settings
from django.urls import path, include

from api.routers import routers

urlpatterns = [
    path('api/', routers.api.urls),
]

if settings.DEBUG:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
