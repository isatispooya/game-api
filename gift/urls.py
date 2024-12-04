from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('gift', views.GiftViewSet, basename='gift')

urlpatterns = router.urls



