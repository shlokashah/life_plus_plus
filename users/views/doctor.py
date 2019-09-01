from django.contrib.auth import login
from django.shortcuts import redirect,render
from django.views.generic import CreateView,TemplateView
from ..forms import DoctorSignUpForm
from ..models import User
from django.http import HttpResponse
from prescription import views


class DoctorSignUpView(CreateView):#class based view to register user as doctor.
    model = User
    form_class = DoctorSignUpForm
    template_name = 'registrations/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('prescription:list')