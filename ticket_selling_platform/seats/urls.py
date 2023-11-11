from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SeatViewSet

router = DefaultRouter()
router.register(r'', SeatViewSet, basename='seat')

urlpatterns = [
    path('', include(router.urls)),
]
