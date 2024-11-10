from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "name",
            "email",
            "contact_reason",
            "product_model",
            "message",
        ]
