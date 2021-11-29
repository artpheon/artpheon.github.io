from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    return render(request, 'account/login.html')

def register(request):
    return render(request, 'account/register.html')

def dashboard(request):
    return render(request, 'account/dashboard.html')

def logout(request):
    return redirect('home')