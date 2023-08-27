from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

def home(request):
    return render(request, 'core/home.html')

def login_page(request):
    return render(request, 'core/login.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'core/register.html', {'form': form})
