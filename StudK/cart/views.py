from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CartSerializer
from .models import Cart
from rest_framework.permissions import IsAuthenticated


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Cart.objects.all().filter(user=self.request.user)
        return queryset
