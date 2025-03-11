from django.shortcuts import render
from django.contrib.auth import forms

# Create your views here.
def login_view(request):
    if request.method == "POST":
        # Authenticate and login.
        form = forms.AuthenticationForm(request.POST)
    else: 
        form = forms.AuthenticationForm()