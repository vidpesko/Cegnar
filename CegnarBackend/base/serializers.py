# serializers.py
from rest_framework import serializers
from .models import PersonalSettings


class SocialSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalSettings
        fields = [
            "instagram_url",
            "facebook_url",
            "email",
            "phone_number",
            "workshop_address",
        ]
