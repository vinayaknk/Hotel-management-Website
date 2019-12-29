from django import forms
from . models import Reserve, Roomservice, Meal
from accounts.models import User as Login_User
from datetime import date
from django.contrib.auth import get_user_model
User = get_user_model()


class ReservationForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.HiddenInput(), initial=User.username)
    check_in_date = forms.DateField(widget=forms.SelectDateWidget,label='check_in_date', input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'], initial=date.today)
    check_out_date = forms.DateField(widget=forms.SelectDateWidget,label='check_out_date', input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'], initial=date.today)

    class Meta():
        model = Reserve
        fields = ('name','check_in_date','check_out_date')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # To get request.user.
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = User.objects.filter(username=self.user)
            # Login_User.objects.filter(username__iexact=self.user)
            # Roomservice.objects.filter(username__username__iexact=self.user)

    def clean(self):
        cleaned_data = super().clean()
        checkin = cleaned_data.get('check_in_date')
        checkout = cleaned_data.get('check_out_date')

        if checkin < date.today():
            raise forms.ValidationError("Check in date should not be past date!. Please enter again")
        elif checkout < date.today():
            raise forms.ValidationError("Check out date should not be past date!. Please enter again")
        elif checkout < checkin :
            raise forms.ValidationError("Check Out date should not be less than check in date!. Please enter again")

Meal_Delivery_Time = [
    ('morning','Morning Breakfast'),
    ('lunch','Lunch'),
    ('evening', 'Evening Snacks'),
    ('night', 'Dinner')
]

class RoomServiceForm(forms.ModelForm):

    delivery_time = forms.CharField(widget=forms.Select(choices=Meal_Delivery_Time))

    class Meta:
        model = Roomservice
        fields = ('name', 'meal','delivery_time')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(RoomServiceForm, self).__init__(*args, **kwargs)
        self.fields['meal'].queryset = Meal.objects.all()
        self.fields['name'].queryset = User.objects.filter(username=self.user)
