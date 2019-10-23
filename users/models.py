from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from django.contrib.admin.widgets import AdminDateWidget

class User(AbstractUser): #custom user model to check the type of user
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    license_number = models.CharField(max_length=50,default="Enter Valid License Number")
    date_of_birth = models.DateField(max_length=10,default="2010-10-10")
    blood_group = models.CharField(max_length=10,default="Enter a Valid Blood Group")
    phone_number = PhoneNumberField(null=False, blank=False,default='+41524204242')
