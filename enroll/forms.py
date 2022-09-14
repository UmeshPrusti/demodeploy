from django import forms
from . models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','password']
        widgets = {
        'password': forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        'name' : forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.EmailInput(attrs={'class':'form-control'})
        }