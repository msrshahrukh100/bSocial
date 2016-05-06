from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$',signup,name='signup'),
	url(r'^api/login$',userlogin,name='login'),
	url(r'^api/dashboard1$',userdashboard,name='userdashboard'),
	url(r'^api/logout$',logout_view,name='logout'),
	url(r'^api/chat$',chat,name='chat'),


]