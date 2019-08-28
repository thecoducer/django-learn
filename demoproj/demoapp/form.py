from demoapp.models import Student
from django import forms

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