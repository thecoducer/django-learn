# Learning Django
Django is a Python-based free and open-source web framework, which follows the model-template-view (MTV) architectural pattern. Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself. Python is used throughout, even for settings files and data models.

## A guide to set up Django in a virtual environment

1. Create a folder: django-learn
2. ```cd django-learn```
3. (Skip if already installed) Install Python's virtual environment: ```sudo apt install virtualenv```
4. Create a virtual environment in Python: ```virtualenv -p python3 env```
    > Virtual environment *env* created for the directory *django-learn*
5. Activate *env*: ```source env/bin/activate```
    > **(env)** must appear just prior to the bash prompt
6. Install Django for your virtual environment: ```pip3 install django```
7. Create Django project folders: ```django-admin startproject demoproj```
    > A single project can have multiple apps
8. ```cd demoproj```
    > Inside the *demoproj* directory
9. Create a Django web app: ```python3 manage.py startapp demoapp```
10. ```cd demoapp```
11. Start the app: ```python manage.py runserver```
    > Go to the localhost:8000. If you get to see the page with a green rocket then the Django app is running successfully

## Day 1
- Create a view in ```demoapp/views.py```
- We need to add path in ```demoproj/urls.py``` for each view we create
- Create ```static``` and ```templates``` within ```demoapp``` directory
- Put ```html``` files inside the ```templates``` folder
- ```static``` folder has ```images``` and ```css``` folders that contains images and css files respectively
- Open ```demoproj/settings.py``` and add your app name ```'demoapp'``` to the ```INSTALLED_APPS``` list and also add this line ```[os.path.join(BASE_DIR, 'templates')]``` to TEMPLATES DIRS

## Day 2
- Style ```test3.html``` using an external CSS ```static/css/style.css```
- Style ```home.html``` using an external CSS ```static/css/home.css```
- Put ```javascript``` files inside ```static/js```
- Create a model in ```demoapp/models.py```
    - A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing.
    - Generally, each model maps to a single database table.
    - Each attribute of the model represents a database field.
    - With all of this, Django gives you an
    automatically-generated database-access API.
    - Django’s models provide an **Object-relational Mapping (ORM)** to the underlying database. ORM is a powerful programming technique that makes working with data and relational databases much easier.
    - Refer [docs.djangoproject.com](https://docs.djangoproject.com/en/2.2/topics/db/models/)
    - Refer [djangobook.com](https://djangobook.com/mdj2-models/)
- Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.
    - Create new migrations based on the changes you have made to your models: ```python manage.py makemigrations```
    - Apply and unapply migrations: ```python manage.py migrate```
    - Refer [docs.djangoproject.com](https://docs.djangoproject.com/en/2.2/topics/migrations/)
- Go to ```localhost:8000/admin``` for Django admin
- To create a user: ```python manage.py createsuperuser```
- Register your newly created model with the admin
    - Refer to [Registering models with admin](https://djangobook.com/mdj2-django-admin/)

## Day 3
- To view the ```Student``` model in the form of a table in a browser, we create a html table in a file: ```showstudents.html```
- To create a new entry for a student, we create a html form in ```createstudent.html```
    - To work with forms we need to create a python file: ```demoapp/form.py```
    - Refer [Working with forms](https://docs.djangoproject.com/en/2.2/topics/forms/)
    - ```{% csrf_token %}``` provides *cross site request forgery protection*. Read [this](https://docs.djangoproject.com/en/2.2/ref/csrf/) to know more
    - Each data entry in our model has a unique ```id``` which is an auto-incremented value. We need to use it whenever we have to uniquely identify each row data.
- To delete an entry, we simply write a function in ```views.py``` to do that.
- To edit an entry, we create a form: ```editstudent.html```, fetch the existing data (GET), modify it and submit the changes (POST).
    - **GET**: Parameters remain in browser history because they are part of the URL
    - **POST**: Parameters are not saved in browser history.
    - Read [this](https://www.diffen.com/difference/GET-vs-POST-HTTP-Requests) to learn more about their difference.

## Day 4
- Generating a csv file:
    - ```getcsv``` method static generates a csv file
    - ```getcsv_db``` method generates a csv file dynamically. It fetches data from the ```Student``` model.
    - Refer [Outputting CSV with Django](https://docs.djangoproject.com/en/2.2/howto/outputting-csv/)
- Generating a pdf file:
    - ```pip3 install reportlab```, we need it to output pdf.
    - ```getpdf``` method static generates a pdf file.
    - ```getpdf_db``` method generates a pdf file dynamically. It fetches data from the ```Student``` model.
    - ```getpdf_nice``` method generates a pdf file with a well-formatted table that contains data from the ```Student``` model.
    - Refer [Outputting PDFs with Django](https://docs.djangoproject.com/en/2.2/howto/outputting-pdf/)

## Day 5
- Creating HTML templates:
    - ```base.html``` includes ```header.html``` and ```footer.html```
    - ```index.html``` and ```about.html``` extends the template ```base.html```
- Added two methods in ```views.py``` to work with session:
    - ```setsession``` sets session
    - ```getsession``` fetches session
- Added two methods in ```views.py``` to work with cookies:
    - ```setcookie``` and ```getcookie```
- Read [this](https://www.tutorialspoint.com/What-is-the-difference-between-session-and-cookies) to know that difference between session and cookie
- To send email via Django, we need this library
    ```python 
        from django.core.mail import send_mail
    ```
    and also add these few lines in ```settings.py```
    ```
        EMAIL_USE_TLS = True
        EMAIL_HOST = 'smtp.mail.yahoo.com'
        EMAIL_PORT = 465
        EMAIL_HOST_USER = 'edummy17@yahoo.com'
        EMAIL_HOST_PASSWORD = 'Kolkata@0101'
    ```

## Day 6
- 

## My setup:
- Ubuntu 18.04.3 LTS
- Python 3.6.8
- pip 19.2.2
- virtualenv 16.7.0