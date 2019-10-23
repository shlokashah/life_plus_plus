from PIL import Image
import pytesseract
import os
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from prescription.models import Prescriptions
from prescription import forms
from web3 import Web3
from utils import blockchain
import json
class Prescription():

	def __init__(self):
		pass

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
		self.text = text
		self.image = prescriptions.image
		self.user = prescriptions.username
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

	def view(self ,request ,pk):
		instance = Prescriptions.objects.get(pk=pk)
		text = instance.text
		hash_ = Web3.soliditySha3(['string'],[text])
		hash_hex = hash_.hex()
		
		b = blockchain.Blockchain(url="http://127.0.0.1:7545", abi=abi)
		b.connect()
		exists = b.check_hash(hash_hex)
		return exists , instance

bytecode = "608060405234801561001057600080fd5b506101c6806100206000396000f3fe608060405260043610610046576000357c01000000000000000000000000000000000000000000000000000000009004806366e34cf11461004b578063af5135fd1461009e575b600080fd5b34801561005757600080fd5b506100846004803603602081101561006e57600080fd5b81019080803590602001909291905050506100f1565b604051808215151515815260200191505060405180910390f35b3480156100aa57600080fd5b506100d7600480360360208110156100c157600080fd5b8101908080359060200190929190505050610140565b604051808215151515815260200191505060405180910390f35b60006100fc82610140565b1561010a576000905061013b565b6000829080600181540180825580915050906001820390600052602060002001600090919290919091505550600190505b919050565b60008060009050600090505b60008054905081101561018f578260008281548110151561016957fe5b90600052602060002001541415610184576001915050610195565b80600101905061014c565b60009150505b91905056fea165627a7a72305820577f0c80bf483610360752f4736f01428e4edf66c5102792faaf73951fb4cf2b0029"

abi = json.loads("""[
	{
		"constant": false,
		"inputs": [
			{
				"name": "hash",
				"type": "bytes32"
			}
		],
		"name": "add_hash",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "hash",
				"type": "bytes32"
			}
		],
		"name": "check_existence",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]""")	