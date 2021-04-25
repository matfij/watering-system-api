# Generated by Django 3.2 on 2021-04-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('state', models.IntegerField(choices=[(0, 'Off'), (1, 'On')])),
            ],
        ),
    ]
