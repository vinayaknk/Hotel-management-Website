# Generated by Django 2.2 on 2019-12-19 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0012_meal_roomservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='meal_rate',
            field=models.FloatField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roomservice',
            name='meal_rate',
            field=models.ForeignKey(default=30, on_delete=django.db.models.deletion.CASCADE, related_name='mealrate', to='reservation.Meal'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='roomservice',
            unique_together={('name', 'booked_on')},
        ),
    ]
