from demoapp.models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = "__all__" # takes all fields from our model
        