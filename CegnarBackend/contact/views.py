from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail

from .serializers import OrderSerializer


class OrderAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    Create new order.
    """
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        print(request.POST)
        send_mail(
            "test",
            "here is the message",
            "vidpesko.business@gmail.com",
            ["vid@pesko.si"],
            fail_silently=False,
            auth_user="vidpesko.business",
            auth_password="xvctgbxmvaobncrh",
        )
        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return self.create(request, *args, **kwargs)
