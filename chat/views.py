from django.shortcuts import render,HttpResponse,redirect
from chat.config import RESPONSE_FORMAT
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import copy
from .forms import *
from .models import *
from django.contrib.auth import login , logout,authenticate
from django.contrib.auth.hashers import check_password,make_password 
from django.contrib.auth.decorators import login_required
import json
from django.conf import settings
from datetime import datetime
import re
from django.core.mail import send_mail
from django.contrib import messages
from opentok import OpenTok

API_KEY = '45583722'
API_SECRET = '315893fcf77b91fb13fa1c29a6a3c81801b26cd6'

# Create your views here.

opentok = OpenTok(API_KEY, API_SECRET)
session = opentok.create_session()



def signup(request):
	response = copy.deepcopy(RESPONSE_FORMAT)
	form = Signupform(request.POST or None,request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			instance = form.save(commit=False)
			instance.set_password(request.POST['password'])
			instance.save()
			response['message'] = "Successfully registered!"
			messages.success(request, 'Successfully registered. Login to continue.')
			return redirect('signup')
	context = {'form':form}
	return render(request,'signup.html',context)


def userlogin(request):
	response = copy.deepcopy(RESPONSE_FORMAT)
	form = Loginform(request.POST or None)
	if request.method == 'GET':
		context = {'form':form}
		return render(request,'login.html',context)
	elif request.method == 'POST':
		if form.is_valid():
			user = Users.check_user(**dict(form.cleaned_data))
			if user:
				user.backend = settings.AUTHENTICATION_BACKENDS
				user.online=True
				user.save()
				login(request, user)

				return redirect('userdashboard')
			else:
				messages.error(request,"Invalid login credentials")
				return redirect('login')
		else :
			messages.error(request,"Invalid login credentials")
			return redirect('login')




@login_required(login_url='login')
def userdashboard(request):
	response = copy.deepcopy(RESPONSE_FORMAT)
	user = request.user
	if request.method == 'POST':
		pass

	context = {
	'users' : Users.objects.all().exclude(id=user.id),
	'user' : user,
	}
	return render(request,'dashboard1.html',context)

@login_required(login_url='login')
def chat(request):
	key = API_KEY
	session_id = session.session_id
	token = opentok.generate_token(session_id)
	context = { 'api_key':key, 'session_id':session_id, 'token':token}
	return render(request,'index.html',context)




	


	

def logout_view(request):
	user = request.user
	user.online = False
	user.save()
	logout(request)
	return redirect('signup')
    # Redirect to a success page.
