from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from users.models import (User)


class DoctorSignUpForm(UserCreationForm):#creating a custom form on top of the default UserCreationForm (to specify the user type as doctor)
    class Meta(UserCreationForm.Meta):
        model = User
        fields=['username','license_number','phone_number','date_of_birth','blood_group']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        # user.license_number = super().save(commit=False)
        if commit:
            user.save()
        return user


class PatientSignUpForm(UserCreationForm):#creating a custom form on top of the default UserCreationForm (to specify the user type as patient)
    class Meta(UserCreationForm.Meta):
        model = User
        fields=['username','phone_number','date_of_birth','blood_group']
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
        return user
        