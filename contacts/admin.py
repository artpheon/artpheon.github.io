from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . import models
# Register your models here.

class ContactAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name', )
    search_fields = ('first_name', 'last_name', 'car_title',)
    list_per_page = 25

admin.site.register(models.Contact, ContactAdmin)