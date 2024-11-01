from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SocialSettingsSerializer
from .models import PersonalSettings


class PersonalSettingsAPIView(APIView):
    def get(self, request):
        social_media_settings = PersonalSettings.load(request_or_site=request)
        serializer = SocialSettingsSerializer(social_media_settings)
        return Response(serializer.data)
