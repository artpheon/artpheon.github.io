from django.contrib import admin
from django.utils.html import format_html
from .models import Car

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):                                  # object - a car object, photo - its attr, url is contained in it
        return format_html('<img src="{}" width="40" style="border-radius: 10%;" />'.format(object.photo.url))
    thumbnail.short_description = 'car photo'
    list_display = ('id','thumbnail', 'title', 'state', 'condition', 'price', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'title')
    list_editable = ('is_featured',)
    search_fields = ('title', 'id', 'state', 'model', 'fuel_type')

# Register your models here.
admin.site.register(Car, CarAdmin)