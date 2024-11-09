from django.urls import path
from .views import ProductCategoryAPIView

urlpatterns = [
    path("categories/", ProductCategoryAPIView.as_view(), name="product-categories-api"),
]
