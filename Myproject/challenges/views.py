from django.shortcuts import render
from django.http import HttpResponse



def saturday(request):
    return HttpResponse('this is satueday')


def sunday(request):
    return HttpResponse('this is sunday')