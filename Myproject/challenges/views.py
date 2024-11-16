from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound



def saturday(request):
    return HttpResponse('this is satueday')


def sunday(request):
    return HttpResponse('this is sunday')


def monday(request):
    return HttpResponse('this is monday')


# دینامیک روت میخواییم بسازیم
# def dynamic_days(request,day,description):
#     return HttpResponse(f"Day: {day}, Description: {description}")


# گسترش میدیم فرضا این دیتابیس ما هست
days={
    'saturday':'this is saturday',
    'sunday':'this is sunday',

}
def dynamic_days(request,day,description):
    # day ما اینجا همون کلید دیتابیس ما هس
    day_data=days.get(day)
    if day_data is not None:
        return HttpResponse(f"Day: {day}, Description: {day_data}")
    else:
        return HttpResponseNotFound('day does not existe')