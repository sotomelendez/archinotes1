#-*- coding: utf-8 -*-
from django import forms
from django.forms import widgets


class SignInForm(forms.Form):
    email = forms.EmailField()
    email.widget.attrs = { 'class':'form-control', 'required':True, 'placeholder':'Email'}
    password = forms.CharField(widget=widgets.PasswordInput())
    password.widget.attrs = { 'class':'form-control', 'required':True, 'placeholder':'Password'}

class SignUpForm(forms.Form):
    email = forms.EmailField()
    email.widget.attrs = { 'id':'id_email_sign_up', 'class':'form-control', 'required':True, 'placeholder':'Your email' }
    email_confirm = forms.EmailField()
    email_confirm.widget.attrs = { 'class':'form-control', 'required':True, 'placeholder':'Confirm your email' }
    password = forms.CharField(widget=widgets.PasswordInput())
    password.widget.attrs = { 'id':'id_password_sign_up', 'class':'form-control', 'required':True, 'placeholder':'Create a password'}
    password_confirm = forms.CharField(widget=widgets.PasswordInput())
    password_confirm.widget.attrs = { 'class':'form-control', 'required':True, 'placeholder':'Confirm your email' }