from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser): #custom user model to check the type of user
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    license_number = models.CharField(max_length=50,default="Enter Valid License Number")
    

