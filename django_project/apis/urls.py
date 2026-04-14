from rest_framework.routers import DefaultRouter
from .views import GameEventViewSet, PlayerViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'events', GameEventViewSet)

urlpatterns = router.urls