"""demoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demoapp import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('time/', views.display),
    path('show/', views.show),
    path('msg/', views.msg),
    path('display/', views.disp),
    path('homepage/', views.home),
    path('studentlist/', views.showstudents),
    path('createstudent/', views.createstudent),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('getcsv', views.getcsv),
    path('getcsvdb', views.getcsv_db),
    path('getpdf', views.getpdf),
    path('getpdfdb', views.getpdf_db),
    path('nicepdf', views.getpdf_nice),
    path('', views.rootpage, name='home'),
    path('sample', views.sample),
    path('about', views.about),
    path('setsession', views.setsession),
    path('getsession', views.getsession),
    path('setcookie', views.setcookie),
    path('getcookie', views.getcookie),
    path('sendmail', views.sendmail),
    path('add', views.add),
    path('login/', LoginView.as_view()),
    path('customreg/', views.customreg)
]
