from django.shortcuts import render, redirect
from django.contrib import messages
from . import models

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        user_id = request.POST['user_id']
        car_title = request.POST['car_title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone_num = request.POST['phone_num']
        message = request.POST['message']

        if request.user.is_authenticated:
            contact = models.Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if contact:
                messages.error(request, "You have already sent an inquiry about this car. We will get back to you as soon as possible to discuss the details.")
                return redirect('/cars/'+car_id)

        contact = models.Contact(
            car_id=car_id,
            user_id=user_id,
            car_title=car_title,
            first_name=first_name,
            last_name=last_name,
            customer_need=customer_need,
            city=city,
            state=state,
            email=email,
            phone_num=phone_num,
            message=message,
        )

        contact.save()
        messages.success(request, "Your request has been sent! Thank you. We will get back to you shortly.")
        return redirect('/cars/'+car_id)