# Learning Django
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
