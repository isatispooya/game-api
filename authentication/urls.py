from django.urls import path
from .views import OtpViewSet, LoginViewSet, OtpSejamViewSet, VerifyOtpSejamViewSet



urlpatterns = [
    path('otp/', OtpViewSet.as_view(), name='otp'),
    path('login/', LoginViewSet.as_view(), name='login'),
    path('otp-sejam/', OtpSejamViewSet.as_view(), name='otp-sejam'),
    path('verify-otp-sejam/', VerifyOtpSejamViewSet.as_view(), name='verify-otp-sejam'),
]
