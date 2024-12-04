from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Missions
from authentication.models import User
from .serializers import MissionsSerializer
from rest_framework.permissions import IsAuthenticated


class MissionsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Missions.objects.all()
    serializer_class = MissionsSerializer
    


