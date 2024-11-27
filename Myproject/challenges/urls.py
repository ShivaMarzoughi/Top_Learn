from django.urls import path
from .views import saturday,sunday,dynamic_days,dynamic_days_by_number

# ترتیب قرار گرفتن این لینک ها مهم
urlpatterns = [
    path('saturday/',saturday),
    path('sunday/',sunday),
    # این اسم دی داینامیک هست
    # path('<day>/',dynamic_days),
    # میشه گسترده ترش هم کرد
    # path('<day>/<description>/', dynamic_days),
    # درست تر مینویسیم
    path('<int:day>/',dynamic_days_by_number),
    path('<str:day>/', dynamic_days,name='days-of-weeks')

]