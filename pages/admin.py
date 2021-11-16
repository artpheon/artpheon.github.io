from django.contrib import admin
from .models import TeamMember
from django.utils.html import format_html

class TeamMemberAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 10px;"/>'.format(object.photo.url))
    thumbnail.short_description = 'Pic'
    list_display = ('id', 'thumbnail', 'first_name', 'speciality', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name')

# Register your models here.
admin.site.register(TeamMember, TeamMemberAdmin)