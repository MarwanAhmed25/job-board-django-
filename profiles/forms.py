from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = [
            'image',
            'code',
            'phone',
            'birthdate',
            'description'
        ]
