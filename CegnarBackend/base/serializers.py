from rest_framework import serializers
from wagtail.images.api.fields import ImageRenditionField

from .models import PersonalSettings


class SocialSettingsSerializer(serializers.ModelSerializer):
    logo = ImageRenditionField("fill-100x100")

    class Meta:
        model = PersonalSettings
        fields = [
            "instagram_url",
            "facebook_url",
            "email",
            "phone_number",
            "workshop_address",
            "workshop_address_raw",
            "logo",
        ]
