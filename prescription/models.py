from django.db import models
from users.models import (User)
class Prescriptions(models.Model):
	record = models.CharField(max_length=100)#check out about the unique field
	image = models.ImageField(upload_to='documents/',blank=False)
	username = models.ForeignKey(User,default=None,on_delete=models.PROTECT)
	text = models.TextField(default="")
	name = models.CharField(default="name",max_length=100)
	def __str__(self):
		return self.record
		
	def delete(self,*args,**kwargs):
		self.image.delete()
		super().delete(*args,**kwargs)
# Create your models here.
#Model prescription.
class XRay(models.Model):
	image = models.ImageField(upload_to='xrays/',blank=False)
	username = models.ForeignKey(User,default=None,on_delete=models.PROTECT)
	name = models.CharField(default="name",max_length=100)
	predictions = models.TextField(default="")
	def __str__(self):
		return self.image.path

	def delete(self , *args , **kwargs):
		self.image.delete()
		super().delete(*args,**kwargs)	 