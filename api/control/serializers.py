from rest_framework.serializers import ModelSerializer

from control.models import Pump


class PumpSerializer(ModelSerializer):

    class Meta:
        model = Pump
        fields = '__all__'
