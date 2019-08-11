from django.urls import path
from .views import users
 
app_name = 'users'

urlpatterns=[
	path('', users.home , name="home"),#website loads here
	# path('register/',views.register_view,name="register"),
	# path('login/',views.login_view,name="login"),
	# path('logout/',views.logout_view,name='logout')
]