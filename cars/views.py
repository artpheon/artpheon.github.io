from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.

def cars(request):
    cars = models.Car.objects.order_by('-created_date')
    data = {
        'cars': cars
    }
    return render(request, 'cars/cars.html', data)

def car_detailed(request, id):
    car = get_object_or_404(models.Car, pk=id)
    if car.num_owners == "0":
        car.num_owners = "N/A"
    data = {
        'car': car,
    }
    return render(request, 'cars/car_detailed.html', data)