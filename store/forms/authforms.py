from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomerAuthform(AuthenticationForm):
    username = forms.EmailField(required=True, label='Email')

class CustomerCreationForm(UserCreationForm):
    username = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=True, label='Last Name')

    def clean_first_name(self):
        value=self.cleaned_data.get('first_name')
        if len(value.strip())<3:
            raise ValidationError('minimum 3 char required')
        return value


    def clean_last_name(self):
        value=self.cleaned_data.get('last_name')
        if len(value.strip())<3:
            raise ValidationError('minimum 3 char required')
        return value


    class Meta:
        model = User
        fields=['username','first_name','last_name']