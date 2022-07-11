from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Style, Material, Colour, Handle, Facade, Slab
from .serializers import StyleSerializer, MaterialSerializer, ColourSerializer, HandleSerializer, FacadeSerializer, \
    SlabSerializer
from cart.models import Cart
from .permissions import ReadOnly, IsAdminUser
from .messaging import send_telegram


class StylesViewSet(viewsets.ModelViewSet):
    serializer_class = StyleSerializer
    permission_classes = [IsAdminUser | ReadOnly]

    def get_queryset(self):
        queryset = Style.objects.all()
        return queryset


class MaterialsViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialSerializer
    permission_classes = [IsAdminUser | ReadOnly]

    def get_queryset(self):
        queryset = Material.objects.all()
        return queryset


class ColoursViewSet(viewsets.ModelViewSet):
    serializer_class = ColourSerializer
    permission_classes = [IsAdminUser | ReadOnly]

    def get_queryset(self):
        queryset = Colour.objects.all()
        return queryset


class HandlesViewSet(viewsets.ModelViewSet):
    serializer_class = HandleSerializer
    permission_classes = [IsAdminUser | ReadOnly]

    def get_queryset(self):
        queryset = Handle.objects.all()
        return queryset


class FacadesViewSet(viewsets.ModelViewSet):
    serializer_class = FacadeSerializer
    permission_classes = [IsAdminUser | ReadOnly]

    def get_queryset(self):
        queryset = Facade.objects.all()
        return queryset


class SlabsViewSet(viewsets.ModelViewSet):
    serializer_class = SlabSerializer
    permission_classes = [IsAdminUser | ReadOnly]

    def get_queryset(self):
        queryset = Slab.objects.all()
        return queryset


class Messaging(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        userProduct = Product.objects.get(id=1)
        userCart = Cart.objects.filter(user=request.user)
        message = "Name: {0}\n" \
                  "Surname: {1}\n" \
                  "email: {2}\n" \
                  "Products: \n".format(request.user.first_name, request.user.last_name, request.user.email)

        for item in userCart:
            message += "{0}\n" \
                      "url: {1}\n" \
                       "----------\n".format(item.product, "http://127.0.0.1:8000/api/v1/products/" + str(item.product.id))

        send_telegram(message)
        return Response(message)


sets = [("styles", StylesViewSet), ("materials", MaterialsViewSet), ("colors", ColoursViewSet),
        ("handles", HandlesViewSet), ("facades", FacadesViewSet), ("slabs", SlabsViewSet)]
