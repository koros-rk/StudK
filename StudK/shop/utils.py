from rest_framework import viewsets
from .models import Style, Material, Colour, Handle, Facade, Slab
from .serializers import StyleSerializer, MaterialSerializer, ColourSerializer, HandleSerializer, FacadeSerializer, SlabSerializer
from .permissions import ReadOnly, IsAdminUser


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


sets = [("styles", StylesViewSet), ("materials", MaterialsViewSet), ("colors", ColoursViewSet),
        ("handles", HandlesViewSet), ("facades", FacadesViewSet), ("slabs", SlabsViewSet)]
