from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        models =SignUp
        # this order really matters how fields are displayed
        fields=["full_name","email"]

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not domain == 'KE':
            raise forms.ValidationError("please provide a kenyan email")
        if not extension == "edu":
            raise forms.ValidationError("please use a valid edu email")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data
        #write validation Code
        return full_name
