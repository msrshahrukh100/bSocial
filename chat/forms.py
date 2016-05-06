from .models import *
from django import forms

class Signupform(forms.ModelForm):
	password = forms.CharField(min_length=5)
	class Meta:
		model = Users
		fields = ["name","email","password","address","phonenumber","image"]


class Loginform(forms.Form):
	email = forms.EmailField()
	password = forms.CharField()





