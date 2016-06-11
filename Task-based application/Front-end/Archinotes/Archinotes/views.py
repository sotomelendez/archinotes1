from django.shortcuts import render, redirect
from forms import *

def index(request):
	return render(request, 'home.jade', {'sign_in_form':SignInForm(), 'sign_up_form':SignUpForm()})

def about(request):
	return render(request, 'about.jade', {'sign_in_form':SignInForm()})

def sign_in(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		return redirect('mgmt:home')

def sign_up(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password'] 
		return redirect('mgmt:home')