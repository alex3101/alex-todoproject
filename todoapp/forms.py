from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Todo,Profile

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=40)

    class Meta:
       model = User
       fields = ['username', 'first_name','password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'deadline', 'status']

class TodoEditForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

class TodoEditStatusForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['status']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'image', 'bio']
