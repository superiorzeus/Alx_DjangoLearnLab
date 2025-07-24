from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# WEEK 11
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# WEEK 11

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'date_of_birth', 'profile_photo') # Add your custom fields

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'date_of_birth', 'profile_photo') # Add your custom fields