from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models

# Create your views here.

def cars(request):
    cars = models.Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'cars': paged_cars
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

def search(request):
    return render(request, 'cars/search.html')