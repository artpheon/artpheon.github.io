from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.

def cars(request):
    return render(request, 'cars/cars.html')

def car_detailed(request, id):
    car = get_object_or_404(models.Car, pk=id)
    data = {
        'car': car,
    }
    return render(request, 'cars/car_detailed.html', data)