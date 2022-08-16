from rest_framework import viewsets
from daycalendar.models import Calendar
from daycalendar.serializer import CalendarSerializer

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer