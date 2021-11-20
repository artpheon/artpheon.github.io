from django.shortcuts import render
from .models import TeamMember
from cars.models import Car

# Create your views here.
def home(request):
    members = TeamMember.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_date')
    for car in featured_cars:
        car.old_price = int(car.price * 1.25)
    data = {
        'members': members,
        'featured_cars': featured_cars,
        'latest_cars': latest_cars,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    members = TeamMember.objects.all()
    data = {
        'members': members,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')