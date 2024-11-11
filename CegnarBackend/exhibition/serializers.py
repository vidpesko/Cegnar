from rest_framework import serializers

from .models import ProductCategory, GalleryImage, GalleryActualImage
from .fields import RawImageField


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            "name",
            "super_category",
        ]


class ActualImageSerializer(serializers.ModelSerializer):
    image = RawImageField(scale_factor=0.4)
    full_image = serializers.SerializerMethodField("get_full_image")

    def get_full_image(self, obj):
        if obj.image:
            return RawImageField().to_representation(obj.image)
        else:
            return None

    class Meta:
        model = GalleryActualImage
        fields = [
            "image",
            "full_image",
        ]


class ProductSerializer(serializers.ModelSerializer):
    image = ActualImageSerializer(many=True)
    category = ProductCategorySerializer()

    class Meta:
        model = GalleryImage
        fields = [
            "id",
            "name",
            "image_description",
            "image",
            "category",
        ]
