from django.shortcuts import render
from .models import TeamMember

# Create your views here.
def home(request):
    team = dict()
    team['team'] = TeamMember.objects.all()
    return render(request, 'pages/home.html', team)

def cars(request):
    return render(request, 'pages/cars.html')

def about(request):
    team = dict()
    team['team'] = TeamMember.objects.all()
    return render(request, 'pages/about.html', team)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')