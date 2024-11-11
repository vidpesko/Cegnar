from django.urls import path
from .views import ProductCategoryAPIView, ProductAPIView, ProductDetailAPIView

urlpatterns = [
    path("categories/", ProductCategoryAPIView.as_view(), name="product-categories-api"),
    path("", ProductAPIView.as_view(), name="product-api"),
    path("<int:pk>", ProductDetailAPIView.as_view(), name="product-detail-api"),
]
