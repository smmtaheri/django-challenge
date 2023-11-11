from rest_framework.routers import DefaultRouter
from .views import StadiumViewSet

router = DefaultRouter()
router.register(r'', StadiumViewSet, basename='stadium')
urlpatterns = router.urls
