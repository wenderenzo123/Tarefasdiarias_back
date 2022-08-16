from django.contrib import admin
from daycalendar.models import Calendar

class Calendars(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'data', 'tempo')
    search_fields = ('titulo', 'descricao', 'data', 'tempo')
admin.site.register(Calendar, Calendars)
    


