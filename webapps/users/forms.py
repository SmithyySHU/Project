from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField(label = 'Email Address' , help_text = 'Enter a valid email address')
    class Meta:
        model = User
        fields = ['username','first_name' , 'last_name' , 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm) :
    email = forms.EmailField(label = 'Email Address' , help_text = 'Enter a valid email address')
    class Meta:
        model = User
        fields = ['username','first_name' , 'last_name' , 'email']

class ProfileUpdateForm(forms.ModelForm) :
    class Meta:
        model = Profile
        fields = ['image']


 