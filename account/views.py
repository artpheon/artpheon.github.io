from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        print("<Received POST request>")
    elif request.method == 'GET':
        print('<Received GET request>')
    return render(request, 'account/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, 'Entered passwords do not match')
            return redirect('register')
        elif User.objects.filter(username=username).exists:
            messages.error(request, 'Username already exists')
            return redirect('register')
        elif User.objects.filter(email=email).exists:
            messages.error(request, 'This email is already used')
            return redirect('register')
        else:
            user = User.objects.create_user(firstname=firstname, lastname=lastname, username=username, email=email, password=password)
            user.save()
            return redirect('register')


        # print('got POST request')
        # return redirect('register')
    return render(request, 'account/register.html')

def dashboard(request):
    return render(request, 'account/dashboard.html')

def logout(request):
    return redirect('home')