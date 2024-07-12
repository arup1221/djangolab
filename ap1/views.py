import datetime
from django.http import HttpResponse
from django.shortcuts import render

def current_dateandtime(request):
    now   = datetime.datetime.now();
    result = "<html><body><h1> current date and time is :%s" %(now)
    return HttpResponse(result)

def four_hours_ahead(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours=4)
    result = "<html><body><h1> After 4 hours, it will be :%s </h1>" %(dt)
    return HttpResponse(result)

def four_hours_before(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours=-4)
    result = "<html><body><h1> Before 4 hours, it was :%s </h1>" %(dt)
    return HttpResponse(result)