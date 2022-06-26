
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import  ModelForm
from .models import Sandogh , Lottory


class SingUpForm(UserCreationForm):
    username = forms.TextInput()
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailInput()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
   
    class Meta:
        model = User
        fields =('username','first_name','last_name','email','password1','password2')
       

class SandoghForm(ModelForm):
    class Meta :
        model = Sandogh
        exclude = (' date_created','time')


class LottoryForm(ModelForm):
    class Meta :
        model = Lottory
        exclude = ('created','name','family')



