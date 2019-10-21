from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import DoctorSignUpForm,PatientSignUpForm
from .models import User

# admin.site.register(Patient)
admin.site.register(User)
