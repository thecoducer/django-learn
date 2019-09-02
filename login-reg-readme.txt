Steps for login/registration:


Step 1:
Go to URLS .py and add the following import

from django.contrib.auth.views import LoginView

Add the following url  to the list of urls:
path('login/',LoginView.as_view())
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Step 2:

Go to the templates folder within your app folder:
Create a folder called registration inside it.
Inside the registration folder create a template file called login.html

<!DOCTYPE html>  
<html lang="en">  
<head>  
     <title>Login</title>  
</head>  
<body>  
<form method="POST" action="/check/">  
        {% csrf_token %}  
        {{ form.as_p }}  
        <button type="submit">Sign In</button>  
</form> 

<br>
<a href="/customreg/">New User?Click here to Sign Up</a>
</body>  
</html>  

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Step 3

Run the file with the url:

localhost:8000/login

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Step 4

To create the registration section:

Go to models.py and add the following import

from django.contrib.auth.models import User

Create the following model class:

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=30)
    dob = models.DateField()
    location=models.CharField(max_length=30)


Step 5
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Stop the server if running by using Ctrl +C in command prompt

Then perform database migration:

python manage.py makemigrations
python manage.py migrate

Step 6
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Register the model in admin.py
Add the following import to admin.py

from djangoapp.models import UserData
Then add the following :

admin.site.register(UserData)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Step 7

Go to form.py
Add the following lines to import:

from djangoapp.models import UserData
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

Create the following forms:

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','password1','password2')


        
class RegForm(forms.ModelForm):
    dob=forms.DateField(label='Date of Birth')
    choices=[('male','Male'),
         ('female','Female')]

    gender = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    
    class Meta:
        model=UserData
        fields=('bio','gender','dob','location')
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 8

Go to views.py 
Add the following function:

def customreg(request):
    if request.method=="POST":
        user=UserForm(request.POST)
        form=RegForm(request.POST)
        if user.is_valid() and form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            user.save()
            profile.save()
            return redirect("/login/")
    else:
        user=UserForm()
        form=RegForm()
    return render(request,"registration/customreg.html",{'form':form,'user':user})


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 9

Go to registration folder within templates folder and create the customreg.html template:

<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Index</title>  
</head>  
<body>  
<form method="POST">  
        {% csrf_token %}
	{{ user.as_p }}  		
        {{ form.as_p }}  
        <button type="submit">Sign Up</button>  
</form> 
<br>
<a href="/login/">Click here to login</a>
</body>  
</html>  


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Step 10

Add the URL mapping in urls.py

path('customreg/',views.customreg)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Step 11

Start the server with the command:
python manage.py runserver

Run the file with the url:

localhost:8000/login

Click on the new user link, it will open up the sign up form
On successful sign up it will redirect to login page
