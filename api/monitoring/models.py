from django.db.models import Model, AutoField, CharField, FloatField, IntegerField


class Plant(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)


class GetHumiditySampleListParams:
    SAMPLES_DEFAULT = 100

    def __init__(self, data: dict):
        self.plant_id = data.get('plantId')
        self.samples = data.get('samples', self.SAMPLES_DEFAULT)



class HumiditySample(Model):
    id = AutoField(primary_key=True)
    plant_id = IntegerField(default=0)
    value = FloatField()
    date = CharField(max_length=255)
