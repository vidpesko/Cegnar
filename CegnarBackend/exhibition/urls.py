from django.urls import path
from .views import ProductCategoryAPIView, ProductAPIView

urlpatterns = [
    path("categories/", ProductCategoryAPIView.as_view(), name="product-categories-api"),
    path("", ProductAPIView.as_view(), name="product-api"),
]
