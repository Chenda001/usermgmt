from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']

        class EditProfileForm(forms.ModelForm):
           class Meta:
              model = CustomUser
              fields = ['username', 'email', 'phone', 'first_name', 'last_name']