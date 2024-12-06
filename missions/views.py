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
        elif mission == 3 : 
            mission = Missions.objects.filter(user=user).first()
            if not mission:
                return Response({"error": "ماموریت یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
            mission.puzzle_done = True
            mission.puzzle_score = 100
            mission.puzzle_end_date = timezone.now()
            mission.save()
            return Response({"message": "ماموریت با موفقیت ثبت شد"}, status=status.HTTP_200_OK)
        
        elif mission == 4 : 
            mission = Missions.objects.filter(user=user).first()
            if not mission:
                return Response({"error": "ماموریت یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
            mission.coffee_done = True
            mission.coffee_score = 100
            mission.coffee_end_date = timezone.now()
            mission.save()
            return Response({"message": "ماموریت با موفقیت ثبت شد"}, status=status.HTTP_200_OK)
        
        elif mission == 5 : 
            mission = Missions.objects.filter(user=user).first()
            if not mission:
                return Response({"error": "ماموریت یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
            question_score_1 = request.data.get('question_score_1')
            mission.test_question_1_score = question_score_1
            mission.test_question_1_done = True
            mission.test_question_1_end_date = timezone.now()
            mission.save()
            return Response({"message": "ماموریت با موفقیت ثبت شد"}, status=status.HTTP_200_OK)
        
        elif mission == 6 : 
            mission = Missions.objects.filter(user=user).first()
            if not mission:
                return Response({"error": "ماموریت یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
            question_score_2 = request.data.get('question_score_2')
            mission.test_question_2_score = question_score_2
            mission.test_question_2_done = True
            mission.test_question_2_end_date = timezone.now()
            mission.save()
            return Response({"message": "ماموریت با موفقیت ثبت شد"}, status=status.HTTP_200_OK)
        
        elif mission == 7 : 
            mission = Missions.objects.filter(user=user).first()
            if not mission:
                return Response({"error": "ماموریت یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
            question_score_3 = request.data.get('question_score_3')
            mission.test_question_3_score = question_score_3
            mission.test_question_3_done = True
            mission.test_question_3_end_date = timezone.now()
            mission.save()
            return Response({"message": "ماموریت با موفقیت ثبت شد"}, status=status.HTTP_200_OK)
        
        elif mission == 8 : 
            mission = Missions.objects.filter(user=user).first()
            if not mission:
                return Response({"error": "ماموریت یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
            photo = request.FILES.get('photo')
            mission.photo = photo
            mission.upload_photo_done = True
            mission.upload_photo_score = 100
            mission.upload_photo_end_date = timezone.now()
            mission.save()
            return Response({"message": "ماموریت با موفقیت ثبت شد"}, status=status.HTTP_200_OK)
        
        else : 
            return Response({"error": "ماموریت یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
        
           
        
    def get(self, request):
        user = request.user
        
        mission_user = Missions.objects.filter(user=user).first()
        if not mission_user:
            return Response({"error": "ماموریت کاربر یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer_mission_user = MissionsSerializer(mission_user).data
        total_score_user = sum(value for field_name, value in serializer_mission_user.items() if field_name.endswith('_score') and value is not None)
        
        mission_all_user = Missions.objects.all()
        response_data = []
        
        for mission in mission_all_user:
            serializer_mission = MissionsSerializer(mission).data
            total_score = sum(value for field_name, value in serializer_mission.items() if field_name.endswith('_score') and value is not None)
            
            end_date_fields = [
                mission.puzzle_end_date, mission.sejam_end_date, 
                mission.broker_end_date, mission.test_question_1_end_date,
                mission.test_question_2_end_date, mission.test_question_3_end_date,
                mission.test_question_4_end_date, mission.coffee_end_date,
                mission.upload_photo_end_date
            ]
            
            valid_times = [date.timestamp() for date in end_date_fields if date is not None]
            avg_completion_time = None
            
            if len(valid_times) >= 1:
                try:
                    avg_completion_time = sum(valid_times) / len(valid_times)
                except Exception:
                    avg_completion_time = None
            
            user_data = {
                "user_name": mission.user.first_name,
                "user_id": mission.user.username,
                "total_score": total_score,
                "avg_completion_time": avg_completion_time,
                "is_authenticated_user": mission.user == user
            }
            response_data.append(user_data)
        
        df = pd.DataFrame(response_data)
        df['avg_completion_time'] = 1733461200 - df['avg_completion_time']
        df['rank'] = df.apply(lambda x: (x['total_score'], -x['avg_completion_time']), axis=1).rank(method='min', ascending=False).astype(int)
        df = df.sort_values(['rank'], ascending=[True])
        df['avg_completion_time'] = df['avg_completion_time'].apply(lambda x: pd.to_datetime(x, unit='s'))
        

        
        
        authenticated_user_data = df[df['is_authenticated_user']].iloc[0]
        user_rank = int(authenticated_user_data['rank'])
        user_score = int(authenticated_user_data['total_score'])
        
        response_data = df.to_dict('records')
        
        response = {
            "user_rank": user_rank,
            "user_score": user_score,
            "all_users": response_data
        }
        
        return Response(response, status=status.HTTP_200_OK)
     

    
class ShowUserMission(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        mission = Missions.objects.filter(user=user).first()
        if not mission:
            return Response({"error": "ماموریت کاربر یافت نشد"}, status=status.HTTP_404_NOT_FOUND)
        serializer_mission = MissionsSerializer(mission).data
        total_score = sum(value for field_name, value in serializer_mission.items() if field_name.endswith('_score') and value is not None)
        response = {
            "total_score": total_score,
            "mission": serializer_mission
        }
        return Response(response, status=status.HTTP_200_OK)
    


