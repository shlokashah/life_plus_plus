from django.db import models
from users.models import (User)
class Prescriptions(models.Model):
	record = models.CharField(max_length=100)
	image = models.ImageField(upload_to='documents/',blank=False)
	username = models.ForeignKey(User,default=None,on_delete=models.PROTECT)
	def __str__(self):
		return self.record
# Create your models here.
#Model prescription.