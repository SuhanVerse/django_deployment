from django import forms
from django.core.validators import RegexValidator
from django.utils import timezone
from .models import Registration
import re


class RegistrationForm(forms.Form):
    # Name field
    name = forms.CharField(
        max_length=100,
        error_messages={'required': 'Name is required'}
    )

    # Email field
    email = forms.EmailField(
        error_messages={
            'required': 'Email is required',
            'invalid': 'Please enter a valid email'
        }
    )

    # Password field
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Password is required'}
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Registration.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Registration.objects.filter(name=name).exists():
            raise forms.ValidationError('This name is already registered.')
        return name

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if not len(password) >= 8 :
    #         raise forms