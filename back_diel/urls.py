from django.contrib import admin
from django.urls import path, include
from daycalendar.views import CalendarViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('calendar', CalendarViewSet,basename='Calendar')
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
