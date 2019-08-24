from django import forms
from . import models

class UploadPrescription(forms.ModelForm):
	class Meta:
		model=models.Prescriptions
		fields = ['image','record']#required fields(input by user)