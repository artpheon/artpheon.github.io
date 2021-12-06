from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from cars.views import search
from .models import TeamMember
from cars.models import Car
from django.core.mail import send_mail

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
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        phone = request.POST['phone']
        text = request.POST['message']

        admin = User.objects.get(is_superuser=True)
        send_mail(
            'Contact Request: ' + subject,
            'You have a new inquiry from {}:\nEmail: {}\nPhone number: {}\n\n{}'.format(name, email, phone, text),
            'drow0440@gmail.com',
            [ admin.email ],
            fail_silently=False
        )
        messages.success(request, "Your question has been sent!")
    return render(request, 'pages/contact.html')