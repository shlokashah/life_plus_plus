from PIL import Image
import pytesseract
import os
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from prescription.models import Prescriptions
from prescription import forms
class Prescription():
	def ocr(self,request,pk):
		'''
		Converts the image into text form

		prescriptions contains instance of the image
		text stores the plain text obtained from image

		'''
		# if request.method =='POST':
		prescriptions=Prescriptions.objects.get(pk=pk)
		pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
		text = pytesseract.image_to_string(Image.open(prescriptions.image))
		return text,prescriptions

	def upload(self,request):
		'''
		To Upload New Records

		'''
		if request.method == 'POST':
			form = forms.UploadPrescription(request.POST,request.FILES)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.username = request.user
				instance.save()
				pk = instance.pk
				return True , pk
		else:
			form = forms.UploadPrescription()
		return form , -1

	def record_list(self,request):
		'''
		To Display A List of All Existing Records
		'''
		prescriptions=Prescriptions.objects.all()
		return prescriptions

	def delete_record(self,request,pk):
		'''
		To Delete A Particular Record
		'''
		if request.method =='POST':
			prescription = Prescriptions.objects.get(pk = pk)
			prescription.delete()

	