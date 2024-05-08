from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customers


class UserSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class EmployeeSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    employee_id = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'employee_id', 'password1', 'password2']


class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['first_name', 'last_name', 'email', 'password', 'city', 'phone', 'location', 'registration_id']