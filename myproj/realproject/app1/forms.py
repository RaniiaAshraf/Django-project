from django import forms
from .models import Donation
class Donationform(forms.ModelForm):
    class Meta :
        model = Donation
        fields ='__all__'