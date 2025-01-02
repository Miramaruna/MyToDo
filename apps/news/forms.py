from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label="Запомнить меня")
