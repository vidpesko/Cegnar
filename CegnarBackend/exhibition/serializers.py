from rest_framework import serializers

from .models import ProductCategory, GalleryImages
from .fields import RawImageField


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            "name",
            "super_category",
        ]


class ProductSerializer(serializers.ModelSerializer):
    image = RawImageField(scale_factor=0.5)
    category = ProductCategorySerializer()

    class Meta:
        model = GalleryImages
        fields = [
            "image_description",
            "image",
            "category",
        ]
