from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username',required=True,widget=forms.TextInput(attrs={'class' : 'form-control footer-input margin-b-20'}))
    password1 = forms.CharField(label='Parol',required=True,widget=forms.PasswordInput(attrs={'class' : 'form-control footer-input margin-b-20'}))

    password2 = forms.CharField(label='Takroriy Parol',widget=forms.PasswordInput(attrs={'class' : 'form-control footer-input margin-b-20'}))
    
    email = forms.CharField(label='Email',widget=forms.TextInput(attrs={'class' : 'form-control footer-input margin-b-20'}))
    
    first_name = forms.CharField(label='Ism',widget=forms.TextInput(attrs={'class' : 'form-control footer-input margin-b-20'}))
    
    last_name = forms.CharField(label='Familya',widget=forms.TextInput(attrs={'class' : 'form-control footer-input margin-b-20'}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")

    def save(self,commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        
        if commit:  
            user.save()
        return user