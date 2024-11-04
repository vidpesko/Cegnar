from django.urls import path
from .views import PersonalSettingsAPIView

urlpatterns = [
    path("personal/", PersonalSettingsAPIView.as_view(), name="personal-settings-api"),
]
