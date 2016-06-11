from django.shortcuts import render, redirect
from forms import *

def index(request):
    sign_in_form = SignInForm()
    sign_up_form = SignUpForm()
    return render(request, 'home.jade', {'sign_in_form':sign_in_form, 'sign_up_form':sign_up_form})

def about(request):
    sign_in_form = SignInForm()
    return render(request, 'about.jade', {'sign_in_form':sign_in_form})

def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password'] 
        print 'sign_in-EMAIL: ', email
        print 'sign_in-PASSWORD: ', password
        return redirect('mgmt:home')

def sign_up(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password'] 
        print 'sign_up-EMAIL: ', email
        print 'sign_up-PASSWORD: ', password
        return redirect('mgmt:home')