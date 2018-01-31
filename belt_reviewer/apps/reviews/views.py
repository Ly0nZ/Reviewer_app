# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):

	return render(request, 'reviews/index.html')


def user(request):
	if not 'user_id' in request.session:
		return redirect('/')

	users = User.objects.all()
	context = {
		'users': users
	}
	return render(request, 'reviews/user.html', context)


def register(request):
	errors = []
	for key, val in request.POST.items():
		if len(val) < 3:
			errors.append("{} must be at least three characters".format(key))
	if request.POST['password'] != request.POST['confirm_password']:
		errors.append("Password & confirmation do not match.")

	if errors:
		for err in errors:
			messages.error(request, err)
		return redirect('/')

	else:

		hashpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(name=request.POST['name'],\
							alias=request.POST['alias'],\
							email=request.POST['email'],\
							password = hashpw)
		request.session['user_id'] = user.id

	return redirect('/user')

def login(request):
	pass



