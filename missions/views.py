from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Missions
from authentication.models import User
from .serializers import MissionsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import requests
import pandas as pd
from authentication.models import UserProfile
from django.utils import timezone

class MissionsViewSet(APIView):
    permission_classes = [IsAuthenticated ]
    def patch(self, request,mission=None):
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()
        if mission == 2 : 
                
            if not user_profile:
                return Response({"error": " مرحله ی پروفایل کاربری  سجام را انجام دهید"}, status=status.HTTP_404_NOT_FOUND)
            uniqueIdentifier = user_profile.uniqueIdentifier

            mission = Missions.objects.filter(user=user).first()
            if not mission:
                return Response({"error": "ماموریت یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
            
            excel_file = 'broker.xlsx'
            if not excel_file:
                return Response({"error": "فایل اکسل یافت نشد"}, status=status.HTTP_400_BAD_REQUEST)
            
            df = pd.read_excel(excel_file)
            if df.empty:
                return Response({"error": "فایل اکسل خالی است"}, status=status.HTTP_400_BAD_REQUEST)
            
            if 'کدملی' not in df.columns:
                return Response({"error": "کدملی در فایل اکسل یافت نشد"}, status=status.HTTP_400_BAD_REQUEST)
        
            if not (df['کدملی'].astype(str) == str(uniqueIdentifier)).any():
                return Response({"error": "کد ملی شما در لیست مجاز نیست"}, status=status.HTTP_403_FORBIDDEN)
            
            mission.broker_done = True
            mission.broker_score = 100
            mission.broker_end_date = timezone.now()
            mission.save()
            

            return Response({"message": "ماموریت با موفقیت ثبت شد"}, status=status.HTTP_200_OK)
        else : 
            return Response({"error": "ماموریت یافت نشد"}, status=status.HTTP_404_NOT_FOUND)    
        

    


