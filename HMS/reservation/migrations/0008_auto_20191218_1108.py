# Generated by Django 2.2 on 2019-12-18 05:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_auto_20191218_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='booked_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 18, 5, 38, 1, 709762, tzinfo=utc)),
        ),
    ]
