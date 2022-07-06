from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import ProductSerializer
from .filters import ProductFilter
from .permissions import ReadOnly, IsAdminUser
from .paginations import StandardResultsSetPagination


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    permission_classes = [IsAdminUser | ReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Product.objects.all().filter(show=True)
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data

        new_product = Product.objects.create(
            title=data['title'],
            description_shorted=data['description_shorted'],
            description_full=data['description_full'],
            main_photo=data['main_photo'],
            handle=Handle.objects.get(title=data['handle']),
            show=True
        )

        for style in data['styles']:
            style_obj = Style.objects.get(title=style['title'])
            new_product.styles.add(style_obj)

        for material in data['materials']:
            material_obj = Material.objects.get(title=material['title'])
            new_product.materials.add(material_obj)

        for color in data['colors']:
            color_obj = Colour.objects.get(title=color['title'])
            new_product.colours.add(color_obj)

        for photo in data['photos']:
            photo_obj = Photos.objects.create(url=photo['url'])
            new_product.photos.add(photo_obj)

        serializer = ProductSerializer(new_product)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()

        instance.title = data.get('title', instance.title)
        instance.description_shorted = data.get('description_shorted', instance.description_shorted)
        instance.description_full = data.get('description_full', instance.description_full)
        instance.main_photo = data.get('main_photo', instance.main_photo)
        instance.show = data.get('show', instance.show)
        instance.handle = Handle.objects.get(title=data.get("handle", instance.handle))

        if data.get('styles'):
            instance.styles.clear()
            for style in data['styles']:
                new_style = Style.objects.create(title=style["title"])
                instance.styles.add(new_style)

        if data.get('materials'):
            instance.materials.clear()
            for material in data['materials']:
                new_material = Material.objects.create(title=material["title"])
                instance.materials.add(new_material)

        if data.get('colours'):
            instance.colours.clear()
            for color in data['colours']:
                new_color = Colour.objects.create(title=color["title"])
                instance.colours.add(new_color)

        instance.save()

        return Response(data)
