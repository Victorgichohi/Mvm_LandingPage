from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        models =SignUp
        # this order really matters how fields are displayed
        fields=["full_name","email"]
