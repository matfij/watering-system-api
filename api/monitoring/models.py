from django.db.models import Model, AutoField, CharField, FloatField, IntegerField


class Plant(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)


class GetHumidityParams:

    def __init__(self, data: dict):
        self.plant_id = data['plantId']
        try:
            self.samples = data['samples']
        except KeyError:
            self.samples = 100


class HumiditySample(Model):
    id = AutoField(primary_key=True)
    plant_id = IntegerField(default=0)
    value = FloatField()
    date = CharField(max_length=255)
