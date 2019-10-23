# import keras
from prescription import forms
from prescription.models import XRay
from utils import model
import numpy as np
import cv2
import os
import PIL.Image
class XRay_class():
	# path = "./model.h5"
	# ml_model = model.XRayModel(path)

	def __init__(self):
		# self.image = image
		pass
	def upload_xray(self , request):
		# if request.method=="POST":
		# 	form = forms.UploadXRay(request.POST, request.FILES)
		# 	if form.is_valid():
		# 		self.image = request.image
		# 		return True
		# else:
		# 	form = forms.UploadXRay()
		# return form			
		if request.method == 'POST':
			form = forms.UploadXRay(request.POST,request.FILES)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.username = request.user
				instance.save()
				pk = instance.pk
				self.pk = pk
				return True , pk
		else:
			form = forms.UploadXRay()
		return form , -1

	def get_results(self,request,path):
		# ml_model = model.XRayModel(path)
		path = "./model.h5"
		ml_model = model.XRayModel(path)

		ml_model.load_model()

		xray_obj = XRay.objects.get(pk = self.pk)
		# print(type(xray_obj.image))
		# img = np.asarray(xray_obj.image)
		print(os.getcwd())
		print(xray_obj.image.url)
		# path_ = os.path.join('.',xray_obj.image.url)
		path_ = xray_obj.image.path
		print(path_)
		img = cv2.imread(xray_obj.image.path)
		print(type(img))
		print(img.shape)
		img = img/255.0
		img = cv2.resize(img , (224 ,224))
		print(type(img))
		pred = np.argmax(ml_model.model.predict(img.reshape([-1,224,224,3])))
		# pred = np.argmax(ml_model.model.predict(img))[0]
		# if pred==1:
		# 	xray_obj.predictions = "Pneumonia"
		# else:
		# 	xray_obj.predictions = "No Pneumonia"	
		# xray_obj.save()
		if pred ==1:
			return "Pneumonia"
		else:
			return "No Pneumonia"	

			
	def xray_list(self,request):
		xray = XRay.objects.all()
		return xray

	def delete_xray(self,request,pk):
		'''
		To Delete A Particular Record
		'''
		# if request.method =='POST':
		xray = XRay.objects.get(pk = pk)
		xray.delete()