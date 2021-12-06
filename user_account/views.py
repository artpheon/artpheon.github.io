from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from cars.models import Car

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in now.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Wrong username or password, please try again.')
            return redirect('login')
    return render(request, 'user_account/login.html')

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
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'This email is already used')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
            auth.login(request, user)
            messages.success(request, 'You are loggedd in now.')
            return redirect('dashboard')
    return render(request, 'user_account/register.html')

@login_required(login_url='/user_account/login')
def dashboard(request):
    inquiries = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    for inquiry in inquiries:
        car = Car.objects.get(car_id=inquiry.car_id)
        setattr(inquiry, 'car_price', car.price)
    data = {
        'inquiries': inquiries,
    }
    return render(request, 'user_account/dashboard.html', data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')