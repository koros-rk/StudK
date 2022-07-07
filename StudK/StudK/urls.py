from django.contrib import admin
from django.urls import path, include
from shop.views import ProductViewSet
from shop.utils import sets, Messaging
from cart.views import CartViewSet
from .yasg import urlpatterns as doc_urls
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'cart', CartViewSet, basename='carts')
for title, VSet in sets:
    router.register(r""+title, VSet, basename=title)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/message', Messaging.as_view())
]

urlpatterns += doc_urls
