from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.http import HttpResponse

class SignUpView(TemplateView):#to show the default signup view
    template_name = 'registrations/signup.html'

def login_view(request):#function based view to log the user in(for both patients and doctors)
	if request.method =='POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			messages.success(request,"You've logged in successfully!")
			if user.is_patient:
				return redirect("prescription:list")
			else:
				return redirect("prescription:list")
			# return redirect('users:home')
	else:
		form = AuthenticationForm()
	return render(request,"registrations/login.html",{'form':form})

def home(request):#default home page
    if request.user.is_authenticated:
        if request.user.is_doctor:
            pass
        else:
            pass
    return render(request, 'users/home.html')

def logout_view(request):#function based view for logging the users out
	# if request.method == 'POST':
	logout(request)
	messages.success(request,"You've logged out successfully!")
	return redirect('login')