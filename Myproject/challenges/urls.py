from django.urls import path
from . import views


urlpatterns = [
    path('edit-profile/',views.index),
]