import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

from monitoring.models import Plant, HumiditySample, GetHumiditySampleListParams
from monitoring.serializers import PlantSerializer, HumiditySampleSerializer


class PlantViewSet(ModelViewSet):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()


class HumiditySampleViewSet(ModelViewSet):
    serializer_class = HumiditySampleSerializer
    queryset = HumiditySample.objects.all()


@api_view(['GET', 'POST'])
def get_humidity(request):
    body = json.loads(request.body)
    params = GetHumiditySampleListParams(body)

    samples = HumiditySample.objects.filter(plant_id=params.plant_id).order_by('-id')[:params.samples]
    serializer = HumiditySampleSerializer(samples, many=True)
    return Response(serializer.data)
