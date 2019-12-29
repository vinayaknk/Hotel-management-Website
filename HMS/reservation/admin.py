from django.contrib import admin
from . import models

# Register your models here.

class MealAdmin(admin.ModelAdmin):
    list_display = ['meal_id','meal_name','meal_rate']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name','check_in_date','check_out_date','booked_on']

class RoomServiceAdmin(admin.ModelAdmin):
    list_display = ['name','meal','booked_on']

admin.site.register(models.Reserve,ReservationAdmin)
admin.site.register(models.Meal, MealAdmin)
admin.site.register(models.Roomservice, RoomServiceAdmin)
