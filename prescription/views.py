from django.shortcuts import render,redirect
from .models import Prescriptions
from . import forms
from django.core.files.storage import FileSystemStorage
from PIL import Image
import pytesseract

# Create your views here.
# 	
def record_list(request):
	prescriptions=Prescriptions.objects.all()
	return render(request,'prescription/prescription_list.html',{'prescriptions':prescriptions})
def upload(request):
	if request.method == 'POST':
		form = forms.UploadPrescription(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.username = request.user
			instance.save()
			return redirect('prescription:list')
	else:
		form = forms.UploadPrescription()
	return render(request,'prescription/prescription_upload.html',{'form':form})

def delete(request,pk):
	if request.method =='POST':
		prescription = Prescriptions.objects.get(pk = pk)
		prescription.delete()
	return redirect('prescription:list')

def ocr(request,pk):
	if request.method =='POST':
		prescriptions=Prescriptions.objects.get(pk=pk)
		pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
		text = pytesseract.image_to_string(Image.open(prescriptions.image))
	return render(request,'prescription/prescription_ocr.html',{'prescriptions':prescriptions,'text':text})