from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serializers import ProductCategorySerializer, ProductSerializer
from .models import ProductCategory, GalleryImage

class ProductCategoryAPIView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    # Filter based on specified product category (if specified)
    def get_queryset(self):
        product_category = self.request.query_params.get("category")

        if product_category:
            return GalleryImage.objects.filter(category__name=product_category)
        else:
            return GalleryImage.objects.all()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = ProductSerializer
