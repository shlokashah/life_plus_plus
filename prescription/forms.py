from django import forms
from . import models

class UploadPrescription(forms.ModelForm):
	class Meta:
		model=models.Prescriptions
		fields = ['image','record','name']#required fields(input by user)

class VerifyOCRText(forms.ModelForm):
	class Meta:
		model=models.Prescriptions
		fields = ['text']	

class UploadXRay(forms.ModelForm):
	class Meta:
		model = models.XRay
		fields = ['image','name']	