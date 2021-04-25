from rest_framework.viewsets import ModelViewSet

from control.models import Pump
from control.serializers import PumpSerializer


class PumpViewSet(ModelViewSet):
    serializer_class = PumpSerializer
    queryset = Pump.objects.all()
