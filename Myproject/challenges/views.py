from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# def saturday(request):
#     return HttpResponse('this is satueday')


# def sunday(request):
#     return HttpResponse('this is sunday')


# def monday(request):
#     return HttpResponse('this is monday')


# دینامیک روت میخواییم بسازیم
# def dynamic_days(request,day,description):
#     return HttpResponse(f"Day: {day}, Description: {description}")


# گسترش میدیم فرضا این دیتابیس ما هست
days={
    'saturday':'this is saturday',
    'sunday':'this is sunday',

}

# def dynamic_days_by_number(request,day):
#     if day>len(days.keys):
#         return HttpResponseNotFound('day does not existe')
#     # days_name=days.get(day)
#     days_names=list(days.keys())
#     redirect_day=days_names[day -1]
#     redirect_url= reverse('days-of-week',args=[redirect_day])  #/days/
#     return HttpResponseRedirect(redirect_url)

#     # return HttpResponseRedirect(f'/days/{redirect_day}')
#     # return HttpResponse(day)  



# def dynamic_days(request,day,description):
#     # day ما اینجا همون کلید دیتابیس ما هس
#     day_data=days.get(day)
#     if day_data is not None:
#         return HttpResponse(f"Day: {day}, Description: {day_data}")
#     else:
#         return HttpResponseNotFound('day does not existe')
    
def dynamic_days(request,day):
    # day ما اینجا همون کلید دیتابیس ما هس
    day_data=days.get(day)
    if day_data is not None:
        # response_data=f'<h1> Day: {day}, Description: {day_data} </h1>'
        # response_data=render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
        context={
            'data':day_data
        }
        return render(request,'challenges/challeng.html',context)
    else:
        return HttpResponseNotFound('day does not existe')


# def days_list(request):
#     # به صورت داینامیک میسازیم
#     days_list=list(days.keys())
#     list_item=''
#     for day in days_list:
#         url_path=reverse('days-of-week',args=[day])
#         list_item += f'<li> <a href="{url_path}">{day}</a> </li>'

#     content =f'<ul> {list_item} </ul>'

#     # content ='''
#     #     <ul> 
#     #      <li> saturday </li>
#     #     </ul>

#     # '''
#     return HttpResponse(content)