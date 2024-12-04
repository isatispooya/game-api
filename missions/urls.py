from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.MissionsViewSet, basename='missions')

urlpatterns = [
    path('missions/<int:mission>/', views.MissionsViewSet.as_view() , name='missions'),
    path('missions/', views.MissionsViewSet.as_view() , name='missions'),
]

