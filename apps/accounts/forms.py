from django import forms
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, HttpResponseRedirect

from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','location','birth_date')
