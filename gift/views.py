from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Gift
from .serializers import GiftSerializer
from rest_framework.permissions import IsAuthenticated


class GiftViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer

    def get_queryset(self):
        return Gift.objects.filter(user=self.request.user)


