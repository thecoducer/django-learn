from demoapp.models import Student
from django import forms
from demoapp.models import UserData
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = "__all__" # takes all fields from our model

class TestForm(forms.Form):
    name = forms.CharField(label = "Enter name", max_length=30, widget = forms.TextInput(attrs={
        'id': 'fname',
        'required': True,
        'placeholder': 'enter name...',
        'class': 'name'
    }))
    email = forms.CharField(label = "Enter email", max_length=30)
    # name and email are field names

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()


class UserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class RegForm(forms.ModelForm):
    dob = forms.DateField(label='Date of Birth')
    choices=[('male', 'Male'), ('female', 'Female')]

    gender = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    class Meta:
        model = UserData 
        fields=('bio', 'gender', 'dob', 'location')