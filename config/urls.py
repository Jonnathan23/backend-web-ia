from rest_framework import routers
from .api import HistoyViewSet

router = routers.DefaultRouter()

router.register('prediction/history', HistoyViewSet, 'history')

urlpatterns = router.urls