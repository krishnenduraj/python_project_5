from django.http import HttpResponse
from django.shortcuts import render

from . models import place
from . models import teams
# Create your views here.
def demo(request):
    obj = place.objects.all()
    return render(request, "index.html",{'result':obj})

def about(request):

    object = teams.objects.all()
    return render(request,"index.html",{'results':object})

    #name="welcome"
    #return render(request,"multiple.html",{'obj': name})

#def subtract(request):
   # a = int(request.GET['num1'])
   # b = int(request.GET['num2'])
   # result = a - b
    #return render(request, "result.html", {'result': result})

#def multiple(request):
    #m = int(request.GET['num1'])
    #n = int(request.GET['num2'])
    #result = m * n
    #return render(request, "result.html", {'result': result})


