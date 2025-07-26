# WEEK_11

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Book

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name',
                  'date_of_birth', 'profile_photo')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name',
                  'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',
                  'date_of_birth', 'profile_photo')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class ExampleForm(forms.Form):
    # You can add some dummy fields here, or leave it empty if it's just a placeholder
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)