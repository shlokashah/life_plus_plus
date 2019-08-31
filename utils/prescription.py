from PIL import Image
import pytesseract
import cv2
import os


class Prescription():

	def __init__():
		self.text = ""

	def load_image(self , path):
		image = cv2.imread(path)
		self.image = image

	def convert_to_text(self , image , image_path=None):
		"""
		Converts image to text using OCR
		Parameters:
		image: PIL image type
		"""
		if image_path!=None:

	def upload(self,request):
		"""
		
		"""
		print("Working")
		# if request.method == 'POST':
		# 	form = forms.UploadPrescription(request.POST,request.FILES)