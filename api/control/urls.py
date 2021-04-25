from django.urls import path, include
from rest_framework.routers import DefaultRouter

from control.views import PumpViewSet


router = DefaultRouter()
router.register('pump', PumpViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
