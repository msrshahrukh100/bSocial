from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.hashers import check_password,make_password 
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
# Create your models here.
class UserCustomManager(BaseUserManager):
	def create_user(self, name, email, phonenumber ,address,image,password=None):
		email = self.normalize_email(email)
		user = self.model(name=name,email=email,phonenumber=phonenumber,address=address,image=image)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,name, email, password,**extra_fields):	
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		return self.create_user(name,email,password)

		



class Users(AbstractBaseUser):
	name = models.CharField(max_length=50,null=False, blank=False)
	address = models.CharField(max_length=50,null=False, blank=False)
	phonenumber = models.CharField(max_length=10,null=False, blank=False)
	image = models.FileField(null=True,blank=True)
	email = models.EmailField(max_length=50,null=False,unique=True	)
	online = models.BooleanField(default=False)

	objects = UserCustomManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']




	@classmethod
	def checkemail(cls,email):
		try:
			data = cls.objects.get(email=email)
		except:
			data = None
		return data

	@classmethod
	def check_user(cls,**kwargs):
		pw = kwargs.get('password')
		uid = kwargs.get('email')
		try:
			user = cls.objects.get(email=uid)
		except:
			return None
		if user.check_password(kwargs['password']):
			return user
		else:
			return None
		


	@classmethod
	def create_user(cls,data):
		return cls.objects.create_user(name=data['name'], email=data['email'], phonenumber=data['phonenumber'],address=data['address'], password=data['password'],image=data['image'])

	def __unicode__(self):
		return str(self.id)
