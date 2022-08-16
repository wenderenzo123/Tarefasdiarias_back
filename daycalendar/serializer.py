from rest_framework import serializers
from daycalendar.models import Calendar

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('id', 'titulo', 'descricao', 'data', 'tempo')