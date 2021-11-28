from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models

# Create your views here.

def cars(request):
    cars = models.Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    search_model = models.Car.objects.values_list('model', flat=True).distinct()
    search_year = models.Car.objects.values_list('year', flat=True).distinct()
    search_city = models.Car.objects.values_list('city', flat=True).distinct()
    search_body_style = models.Car.objects.values_list('body_style', flat=True).distinct()
    search_transmission = models.Car.objects.values_list('transmission', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'search_model': search_model,
        'search_year': search_year,
        'search_city': search_city,
        'search_body_style': search_body_style,
        'search_transmission': search_transmission,
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
    # all cars
    cars = models.Car.objects.order_by('-created_date')

    # searching filters
    keyword = None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model'] 
        cars = cars.filter(model__iexact=model)
        
    if 'year' in request.GET:
        year = request.GET['year']
        cars = cars.filter(year__iexact=year)

    if 'city' in request.GET:
        city = request.GET['city']
        cars = cars.filter(city__iexact=city)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    # for search bar
    search_model = models.Car.objects.values_list('model', flat=True).distinct()
    search_year = models.Car.objects.values_list('year', flat=True).distinct()
    search_city = models.Car.objects.values_list('city', flat=True).distinct()
    search_body_style = models.Car.objects.values_list('body_style', flat=True).distinct()
    search_transmission = models.Car.objects.values_list('transmission', flat=True).distinct()

    data = {
        'keyword': keyword,
        'cars': cars,
        'search_model': search_model,
        'search_year': search_year,
        'search_city': search_city,
        'search_body_style': search_body_style,
        'search_transmission': search_transmission,
    }
    return render(request, 'cars/search.html', data)