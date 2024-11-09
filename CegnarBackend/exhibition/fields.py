from collections import OrderedDict

from rest_framework import serializers

from wagtail.images.models import SourceImageIOError


class ProductCategoryField(serializers.Field):
    def to_representation(self, value):
        output = {
            "name": value.name,
            "super_category": value.super_category,
        }
        return output


class RawImageField(serializers.Field):
    def __init__(self, scale_factor=1, *args, **kwargs):
        self.scale_factor = scale_factor
        super().__init__(*args, **kwargs)

    def to_representation(self, image):
        try:
            w, h = round(image.width * self.scale_factor), round(image.height * self.scale_factor)
            filter_spec = f"fill-{w}x{h}"
            thumbnail = image.get_rendition(filter_spec)

            return OrderedDict(
                [
                    ("url", thumbnail.url),
                    ("full_url", thumbnail.full_url),
                    ("width", thumbnail.width),
                    ("height", thumbnail.height),
                    ("alt", thumbnail.alt),
                ]
            )
        except SourceImageIOError:
            return OrderedDict(
                [
                    ("error", "SourceImageIOError"),
                ]
            )
