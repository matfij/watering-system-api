from django.urls import path, include
from rest_framework.routers import DefaultRouter

from monitoring.views import HumiditySampleViewSet, PlantViewSet, get_humidity


router = DefaultRouter()
router.register('humidity', HumiditySampleViewSet)
router.register('plant', PlantViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('humiditySamples/', get_humidity),
]
