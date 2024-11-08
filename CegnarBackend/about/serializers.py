from rest_framework import serializers
from wagtail.images.models import Image
from wagtail.rich_text import expand_db_html
import re


class RichTextWithImagesField(serializers.Field):
    def to_representation(self, value):
        request = self.context.get("request")  # Get request from context
        html = expand_db_html(value)

        embed_pattern = re.compile(r'<img\b[^>]*src="([^"]+)"')

        def replace_embed(match):
            image_relative_url = match.group(1)
            # Build absolute URL for the image
            image_url = (
                request.build_absolute_uri(image_relative_url)
                if request
                else ""
            )
            return match.group(0).replace(image_relative_url, image_url)

        return embed_pattern.sub(replace_embed, html)
