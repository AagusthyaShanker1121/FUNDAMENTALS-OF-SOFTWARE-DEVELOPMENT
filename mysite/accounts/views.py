from django.shortcuts import render, redirect
from django.contrib.auth import forms, logout
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == "POST":
        # Authenticate and login.
        form = forms.AuthenticationForm(request.POST)
    else: 
        form = forms.AuthenticationForm()

def logout_view(request):
    logout(request)
    messages.success(request, "You have been succesfully logged out.")
    return redirect('index')