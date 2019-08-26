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
- View the ```Student``` model in the form of a table in a browser
    - Created a html table in file: ```showstudents.html```
- To create a new entry for a student, we create a html form in ```createstudent.html```
    - To work with forms we need to create a python file: ```demoapp/form.py```
    - Refer [Working with forms](https://docs.djangoproject.com/en/2.2/topics/forms/)
    - ```{% csrf_token %}``` provided cross site request forgery protection. Read [this](https://docs.djangoproject.com/en/2.2/ref/csrf/) to know more
    - Each data entry in our model has a unique ```id``` which is an auto-incremented value. We need to use it whenever we have to uniquely identify each row data.
- To delete an entry. We simply do that writing a function in ```views.py```
- To edit an entry. We create a form: ```editstudent.html```, fetch the existing data (GET), modify it and submit the changes (POST).


## My setup:
- Ubuntu 18.04.3 LTS
- Python 3.6.8
- pip 19.2.2
- virtualenv 16.7.0