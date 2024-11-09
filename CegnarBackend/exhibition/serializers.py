from rest_framework import serializers
from wagtail.images.models import Image
import re


class ProductCategoryField(serializers.Field):
    def to_representation(self, value):
        output = {
            "name": value.name,
            "super_category": value.super_category,
        }
        return output
