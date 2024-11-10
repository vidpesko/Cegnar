from django.urls import path
from .views import OrderAPIView

urlpatterns = [
    path("message/", OrderAPIView.as_view(), name="contact-api"),
]
