"""life_plus_plus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import users,patient,doctor
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),#to go to the admin site
    path('' , include("users.urls")),#default page(page where website loads)
    path('accounts/login/', users.login_view,name='login'),#login the users
    path('accounts/logout/',users.logout_view,name='logout'),#logout the users
    path('accounts/signup/', users.SignUpView.as_view(), name='signup'),#basic signup page,after this asks if you want to register as patient or doctor
    path('accounts/signup/patient/', patient.PatientSignUpView.as_view(), name='patient_signup'),#signup for patient
    path('accounts/signup/doctor/', doctor.DoctorSignUpView.as_view(), name='doctor_signup'),#signup for doctor
    path('record/',include('prescription.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
