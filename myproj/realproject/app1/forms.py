from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Donation, Funded
class Donationform(forms.ModelForm):
    class Meta :
        model = Donation
        fields ='__all__'

class Fund(forms.ModelForm):
    class Meta:
        model = Funded
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']