from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationViewSet

router = DefaultRouter()
router.register(r'register', UserRegistrationViewSet, basename='user-registration')

urlpatterns = router.urls
