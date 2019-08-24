from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'prescription'

urlpatterns=[
	path('upload/',views.upload,name="upload"),
	path('list/',views.record_list,name="list"),
	path('delete/<int:pk>/',views.delete,name="delete"),]
	# path('ocr/',views.ocr,name="ocr")]
