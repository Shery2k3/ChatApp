from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm

def home(request):
    return render(request, 'home.html')

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # save the user object
            user = form.save()
            # log the user in
            login(request, user)
            # redirect to home
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})
