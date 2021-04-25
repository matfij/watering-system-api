from rest_framework.serializers import ModelSerializer

from monitoring.models import HumiditySample, Plant


class PlantSerializer(ModelSerializer):

    class Meta:
        model = Plant
        fields = '__all__'


class HumiditySampleSerializer(ModelSerializer):

    class Meta:
        model = HumiditySample
        fields = '__all__'
