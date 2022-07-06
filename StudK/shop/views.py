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

        for photo in data['photos']:
            photo_obj = Photos.objects.create(url=photo)
            new_product.photos.add(photo_obj)

        for style in data['styles']:
            style_obj = Style.objects.get(title=style)
            new_product.styles.add(style_obj)

        for material in data['materials']:
            material_obj = Material.objects.get(title=material)
            new_product.materials.add(material_obj)

        for color in data['colors']:
            color_obj = Colour.objects.get(title=color)
            new_product.colours.add(color_obj)

        for facade in data['facades']:
            facade_obj = Facade.objects.get(title=facade['title'], thumbnail=facade['thumbnail'],
                                            main_photo=facade['main_photo'])
            new_product.facades.add(facade_obj)

        for slab in data['slabs']:
            slab_obj = Slab.objects.get(title=slab['title'], thumbnail=slab['thumbnail'],
                                        main_photo=slab['main_photo'])
            new_product.slabs.add(slab_obj)

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
                new_style = Style.objects.get(title=style)
                instance.styles.add(new_style)

        if data.get('materials'):
            instance.materials.clear()
            for material in data['materials']:
                new_material = Material.objects.get(title=material)
                instance.materials.add(new_material)

        if data.get('colors'):
            instance.colours.clear()
            for color in data['colors']:
                new_color = Colour.objects.get(title=color)
                instance.colours.add(new_color)

        if data.get('facades'):
            instance.facades.clear()
            for facade in data['facades']:
                new_facade = Facade.objects.get(title=facade['title'], thumbnail=facade['thumbnail'],
                                                main_photo=facade['main_photo'])
                instance.facades.add(new_facade)

        if data.get('slabs'):
            instance.slabs.clear()
            for slab in data['slabs']:
                new_slab = Slab.objects.get(title=slab['title'], thumbnail=slab['thumbnail'],
                                            main_photo=slab['main_photo'])
                instance.slabs.add(new_slab)

        instance.save()
        return Response(data)
