from django.urls import path
from .views import saturday,sunday


urlpatterns = [
    path('saturday/',saturday),
    path('sunday/',sunday)
]