from django.urls import path
from .views import saturday,sunday,dynamic_days


urlpatterns = [
    path('saturday/',saturday),
    path('sunday/',sunday),
    # این اسم دی داینامیک هست
    path('<day>/',dynamic_days),
    # میشه گسترده ترش هم کرد
    path('<day>/<description>/', dynamic_days)


]