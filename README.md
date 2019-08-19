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
    - ```python
        def index(request):
            return HttpResponse("<h1>Hello world!</h1>")
        ```
- We need to add path in ```demoproj/urls.py``` for each view we create
- 

## My setup:
- Ubuntu 18.04.3 LTS
- Python 3.6.8
- pip 19.2.2
- virtualenv 16.7.0