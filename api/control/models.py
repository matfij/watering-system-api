from django.db.models import Model, IntegerChoices, AutoField, IntegerField, CharField


class Pump(Model):

    class PumpState(IntegerChoices):
        OFF = 0
        ON = 1

    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    state = IntegerField(choices=PumpState.choices, default=PumpState.OFF)
