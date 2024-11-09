from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serializers import ProductCategorySerializer
from .models import ProductCategory

class ProductCategoryAPIView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
