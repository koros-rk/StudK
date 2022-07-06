from django.contrib import admin
from django.urls import path, include
from shop.views import ProductViewSet
from shop.utils import sets
from .yasg import urlpatterns as doc_urls
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename="products")
for title, VSet in sets:
    router.register(r""+title, VSet, basename=title)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]

urlpatterns += doc_urls
