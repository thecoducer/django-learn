from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from demoapp.models import Student
from demoapp.form import StudentForm

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello world!</h1>")

def display(request):
	d = datetime.datetime.now()
	return HttpResponse("The current date and time is " + str(d))

def show(request):
    name = "Mayukh"
    return render(request, "test.html", {'uname': name})

def msg(request):
	return render(request, "test2.html")

def disp(request):
    return render(request, "test3.html")

def home(request):
    return render(request, "home.html")

def showstudents(request):
    students = Student.objects.all()
    return render(request, "showstudents.html", {'students': students})

def createstudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/studentlist")
    else:
        form = StudentForm()
        return render(request, "createstudent.html", {'sform': form})

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/studentlist")

def edit(request,id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("/studentlist")
    else: # while GET
        form = StudentForm()
        return render(request, "editstudent.html", {'sform': form, 'student': student})