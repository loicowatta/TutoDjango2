'''
Created on 24 févr. 2018

@author: loico
'''
from django import forms
from TutoDjango.models import Person
from TutoDjango.models import Student
from TutoDjango.models import Employee

class LoginForm(forms.Form):
    email       = forms.EmailField(label='Courriel')
    password    = forms.CharField(label='Mot de passe', 
                                  widget = forms.PasswordInput)
    def clean(self):
        cleaned_data = super (LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        
    #Test validité des données
        if email and password:
            result = Person.objects.filter(password=password, email=email)
            if len(result) !=1:
                raise forms.ValidationError("Adresse de courriel ou mot de passe erroné. ")
        return cleaned_data
    
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ("friends",)
        
class EmployeeProfilForm(forms.ModelForm):
    class Meta:
        model   = Employee
        exclude = ('friends',)
    

        