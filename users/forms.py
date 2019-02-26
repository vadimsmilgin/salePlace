from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SingUp(UserCreationForm):
    account_image = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'account_image')