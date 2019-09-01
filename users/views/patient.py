from django.contrib import messages
from django.contrib.auth import login
from django.db import transaction
from django.db.models import Count
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from ..forms import PatientSignUpForm
from ..models import User
from django.http import HttpResponse

class PatientSignUpView(CreateView):#class based view to register user as patient.
    model = User
    form_class = PatientSignUpForm
    template_name = 'registrations/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('prescription:list')
