from utils import prescription , blockchain ,x_ray
from django.shortcuts import render,redirect
from .models import Prescriptions ,XRay
from . import forms
from django.core.files.storage import FileSystemStorage
from PIL import Image
import pytesseract
from django.http import HttpResponse , HttpResponseRedirect
from web3 import Web3
import json
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import web3
# Create your views here.

# contract_address="0x68C7375827709848F649C2996fC806d10D5514d6"
path = "./model.h5"
print("THIS WORKS")
flag1=False

# Create your views here.
@login_required
def record_list(request):
	trial = prescription.Prescription()
	prescriptions = trial.record_list(request)
	return render(request,'prescription/prescription_list.html',{'prescriptions':prescriptions})

@login_required
def upload(request):
	trial = prescription.Prescription()
	form ,pk = trial.upload(request)
	if pk!=-1:
		# return redirect('prescription:ocr/'+str(pk))
		print("a")
		return HttpResponseRedirect(reverse('prescription:ocr' , args=(pk,)))
		
	else:
		print("b")
		return render(request,'prescription/prescription_upload.html',{'form':form})
		
@login_required
def delete(request,pk):
	trial = prescription.Prescription()
	trial.delete_record(request,pk)
	# pk1 = kwargs.get('pk1', none) 
	return redirect('prescription:list')

@login_required
def ocr(request,pk):
	if request.method == "GET":	
		trial = prescription.Prescription()
		ocr_instance = trial.ocr(request,pk)
		# pk2 = kwargs.get('pk2', none) 
		text = ocr_instance[0]
		prescriptions = ocr_instance[1]
	

	elif request.method == "POST":
		# form = forms.VerifyOCRText(request.POST , request.FILES)
		# if form.is_valid():
		instance = Prescriptions.objects.get(pk = pk)
		if instance is not None:
			instance.text = request.POST.get('ocr-text' , "")
			instance.save()

			instance = Prescriptions.objects.get(pk=pk)
			text = instance.text
			hash_ = Web3.sha3(text=text)
			hash_hex = hash_.hex()
			# print(hash_hex)
			# print(hash_)
			# print(len(hash_hex))
			if flag1==False:
				b = blockchain.Blockchain(url="http://127.0.0.1:7545" , abi=abi)
				# flag1=True
			if b.connect():
				inserted = b.insert_hash(hash_hex)
				print(inserted)
				if inserted:
					return redirect('prescription:list')
				else:
					return HttpResponse('<h1>Push to blockchain failed</h1>')
			else:
				return HttpResponse("<h1>Connection failed</h1>")



			# return redirect('prescription:block' , args=(pk))
			# return render(block(request,pk))
		else:
			return HttpResponse("<h1>Instance is null</h1>")	
	
	return render(request,'prescription/prescription_ocr.html',{'prescriptions':prescriptions,'text':text })


@login_required
def download(request,pk):
	instance = Prescriptions.objects.get(pk=pk)
	text = instance.text
	hash_ = Web3.soliditySha3(['string'],[text])
	hash_hex = hash_.hex()
	if flag1==False:
		b = blockchain.Blockchain(url="http://127.0.0.1:7545", abi=abi)
		# flag1=True
	b.connect()
	exists = b.check_hash(hash_hex)

	if exists:
		return render(request , 'prescription/prescription_download.html' ,{"prescription":instance} )
	else:
		return HttpResponse("<h1>Hash does not exist in blockchain</h1>")	

@login_required
def view(request,pk):
	trial = prescription.Prescription()
	print(trial)
	(exists , instance) = trial.view(request,pk)
	if exists:
		return render(request , 'prescription/prescription_view.html' , {'prescription':instance})
	else:
		return HttpResponse("<h1>Hash does not exist in blockchain</h1>")	

@login_required
def xray(request):
	trial = x_ray.XRay_class()
	form , pk = trial.upload_xray(request)

	if pk!=-1:
		print(pk)
		obj = XRay.objects.get(pk=pk)

		pred = trial.get_results(request , path)   
		print(pred)
		print(obj.predictions)
		obj.predictions = pred
		obj.save()
		image_path = obj.image.url
		return render(request , "prescription/xray_result.html" , {"image_path":image_path,"predictions":pred})	

	# pred = "Nahi aaya"
	return render(request , "prescription/xray_upload.html" , {"form":form})

@login_required
def xray_list(request):
	trial = x_ray.XRay_class()
	xray = trial.xray_list(request)
	return render(request,'prescription/xray_list.html',{'xray':xray})

@login_required
def xray_delete(request,pk):
	# print("deelte ho rha hai" , pk)
	trial = x_ray.XRay_class()
	trial.delete_xray(request,pk)
	return redirect('prescription:xray_list')

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