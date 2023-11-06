from django import forms
from .models import *


class RegistrationForm(forms.Form):
    nickname = forms.CharField(max_length=25, label="Никнейм")
    firstName = forms.CharField(max_length=25, label="Имя")
    lastName = forms.CharField(max_length=25, label="Фамилия")
    email = forms.EmailField(label="E-mail")
    password = forms.PasswordInput()
    confPassword = forms.PasswordInput()
