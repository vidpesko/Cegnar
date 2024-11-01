from django.urls import path
from .views import PersonalSettingsAPIView

urlpatterns = [
    path("social/", PersonalSettingsAPIView.as_view(), name="personal-settings-api"),
]
