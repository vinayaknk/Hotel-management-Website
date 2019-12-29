from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Reserve(models.Model):
     name = models.ForeignKey(User, related_name="reserve", on_delete=models.CASCADE)
     booked_on = models.DateTimeField(default=timezone.now)
     check_in_date = models.DateField(blank=True, null=True)
     check_out_date= models.DateField(blank=True, null=True)

     def __str__(self):
         return str(self.name.username)

     def get_absolute_url(self):
         return reverse('reservation:detail', kwargs={'username': self.name.username, 'pk': self.pk})

     # def get_absolute_url(self):
     #     return reverse("reservation:reserve_detail")

class Meal(models.Model):
    meal_id = models.CharField(max_length=20)
    meal_name = models.CharField(max_length=128)
    meal_rate = models.FloatField(default=30.0)

    def __str__(self):
        return self.meal_name+" : Rs."+str(self.meal_rate)

class Roomservice(models.Model):
    name = models.ForeignKey(User, related_name="roomservice", on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, related_name="mealbook", on_delete=models.CASCADE)
    delivery_time = models.CharField(max_length=64)
    booked_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name.username

    def get_absolute_url(self):
        return reverse('reservation:meal_list', kwargs={'username': self.name.username})

    class Meta:
        unique_together = ('name','booked_on')
