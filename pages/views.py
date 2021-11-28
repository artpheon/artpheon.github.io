from django.shortcuts import render

from cars.views import search
from .models import TeamMember
from cars.models import Car

# Create your views here.
def home(request):
    members = TeamMember.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_date')
    for car in featured_cars:
        car.old_price = int(car.price * 1.25)
    
    # search_fields = Car.objects.values('model', 'year', 'city', 'body_style')
    search_model = Car.objects.values_list('model', flat=True).distinct()
    search_year = Car.objects.values_list('year', flat=True).distinct()
    search_city = Car.objects.values_list('city', flat=True).distinct()
    search_body_style = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'members': members,
        'featured_cars': featured_cars,
        'latest_cars': latest_cars,
        'search_model': search_model,
        'search_year': search_year,
        'search_city': search_city,
        'search_body_style': search_body_style,
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