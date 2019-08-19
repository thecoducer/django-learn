from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello world!</h1>")

def display(request):
	d = datetime.datetime.now()
	return HttpResponse("The current date and time is " + str(d))

def show(request):
    name = "Mayukh"
    return render(request, "test.html", {'uname': name})