from abc import ABC
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class PhotoListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return value.url


class TagListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return value.title


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ('title', )


class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colour
        fields = ('title', )


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('title', )


class HandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handle
        fields = ('title', )


class FacadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facade
        fields = ('title', 'thumbnail', 'main_photo')


class SlabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slab
        fields = ('title', 'thumbnail', 'main_photo')


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')


class ProductSerializer(serializers.ModelSerializer):
    photos = PhotoListingField(many=True, read_only=True)
    styles = TagListingField(many=True, read_only=True)
    materials = TagListingField(many=True, read_only=True)
    colours = TagListingField(many=True, read_only=True)
    facades = FacadeSerializer(many=True, read_only=True)
    slabs = SlabSerializer(many=True, read_only=True)
    handle = TagListingField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description_shorted', 'description_full', 'main_photo', 'photos', 'styles',
                  'materials', 'colours', 'facades', 'slabs', 'handle', 'show', )
