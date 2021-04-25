import json
from rest_framework.viewsets import ModelViewSet

from monitoring.models import Plant, HumiditySample, GetHumidityParams
from monitoring.serializers import PlantSerializer, HumiditySampleSerializer


class PlantViewSet(ModelViewSet):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()


class HumiditySampleViewSet(ModelViewSet):
    serializer_class = HumiditySampleSerializer
    queryset = HumiditySample.objects.all()

    def get_queryset(self):
        body = json.loads(self.request.body)
        params = GetHumidityParams(body)
        return reversed(
            self.queryset.filter(plant_id=params.plant_id).order_by('-id')[:params.samples]
        )
