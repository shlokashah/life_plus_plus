from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'prescription'

urlpatterns=[
path('upload/',views.upload,name="upload"),
path('list/',views.record_list,name="list"),
path('delete/<int:pk>/',views.delete,name="delete"),
path('ocr/<int:pk>',views.ocr,name="ocr"),
path('view/<int:pk>/' , views.view , name="view"),
path('download/<int:pk>/' , views.download , name="download"),
path('xray/' , views.xray , name="xray"),
path('xray_list/',views.xray_list,name="xray_list"),
path('xray_delete/<int:pk>/',views.xray_delete,name="xray_delete"),
# path('ocr/<int:pk2>/delete/<int:pk1>',views.delete,name="goback_delete")
]
