from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import WebhookData


class WebhookAPIView(APIView):
    def post(self, request):
        data = request.data
        WebhookData.objects.create(data=data)
        return Response(status=status.HTTP_200_OK)