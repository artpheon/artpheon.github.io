from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detailed, name='car_detailed'),
    path('search', views.search, name='search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)