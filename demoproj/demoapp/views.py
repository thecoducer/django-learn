from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
# Day 2
from demoapp.models import Student
# Day 3
from demoapp.form import StudentForm
# Day 4
import csv
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

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
        student=Student.objects.get(id=id)
        if request.method=="POST":
                form=StudentForm(request.POST,instance=student)
                if form.is_valid():
                        form.save()
                        return redirect("/studentlist")
        else:
                form=StudentForm()
                return render(request,"editstudent.html",{'sform':form,'student':student})

def getcsv(request):
        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment;filename="student.csv"'
        writer = csv.writer(response)
        writer.writerow(['Id', 'Name', 'Marks'])
        writer.writerow(['100', 'priya', '90'])
        writer.writerow(['101', 'puja', '92'])
        return response

def getcsv_db(request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment;filename="student_db.csv"'
        writer = csv.writer(response)
        students = Student.objects.all()
        writer.writerow(['Fname', 'Lname', 'Email', 'DOB', 'Age'])
        for student in students:
                writer.writerow([student.fname, student.lname, student.email, student.dob, student.age])
        return response

def getpdf(request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition']='attachment;filename="pdf1.pdf"'
        c = canvas.Canvas(response)
        c.setFont("Times-Roman", 42)
        c.drawString(100, 700, "Hello user!")
        c.showPage()
        c.save()
        return response

def getpdf_db(request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition']='attachment;filename="pdf2.pdf"'
        c = canvas.Canvas(response)
        c.setFont("Times-Roman", 22)
        students = Student.objects.all()
        c.drawString(80, 700, "Fname Lname Email DOB Age")
        x = 80
        y = 600
        for student in students:
                c.drawString(x, y, student.fname + " " + student.lname + " " + student.email + " " + str(student.dob) + " " + str(student.age))
                y = y - 30
                c.drawString(x, y, "-------------------------------------------------------------")
                y = y - 100
        c.showPage()
        c.save()
        return response

def getpdf_nice(request):
        doc = SimpleDocTemplate('pdf3.pdf', pagesize=letter)
        elements = []
        header = ['First Name', 'Last Name', 'Email', 'DOB', 'Age']
        students = Student.objects.all()
        data = []

        data.append(header)
        for s in students:
                data.append([s.fname, s.lname, s.email, s.dob, s.age])

        t = Table(data, 5*[1.5*inch], len(data)*[0.4*inch])
        t.setStyle(TableStyle([
                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.blue),
                ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                ]))
        elements.append(t)
        # write the document to disk
        doc.build(elements)
        return HttpResponse("pdf created")

def rootpage(request):
	return render(request, "rootpage.html")
