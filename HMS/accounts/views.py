from django.shortcuts import render
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy
# Create your views here.

class SignUpView(CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

