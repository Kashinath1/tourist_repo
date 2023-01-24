from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def myfunctioncall(request):
    return render(request, 'index.html')

def myfunctionabout(request):
    return HttpResponse("About section")

def intro(request, name, age):
    mydictionary ={
        "name":name,
        "age":age
    }
    return JsonResponse(mydictionary)

def mycommonpage(request):
    return render(request, 'common.html')

def servicespage(request):
    return render(request, 'servicespage.html')