'''
Created on 23 févr. 2018

@author: loico
'''
from django.shortcuts import render, redirect
from TutoDjango.models import Person, Student, Employee, Message
from TutoDjango.forms import LoginForm
from TutoDjango.forms import StudentProfileForm, EmployeeProfilForm


def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        # On cherche un étudiant
        if len(Student.objects.filter(id=logged_user_id)) == 1:
            return Student.objects.get(id=logged_user_id)
        # on cherche un employé
        if len(Employee.objects.filter(id=logged_user_id)) == 1:
            return Employee.objects.get(id=logged_user_id)
        # Si on a rien
        else:
            return None
    else:
        return None

def welcome(request):
    if 'logged_user_id' in request.session:
        logged_user = get_logged_user_from_request(request)
        if logged_user :
            friendMessages = Message.objects.filter(author__friends=logged_user).order_by('-publication_date')
            return render(request, 'welcome.html', 
                  {'logged_user':logged_user,
                   'friendMessages': friendMessages})
             
            
        
    else:
        return redirect('/login')

def login(request):
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            logged_user = Person.objects.get(email=user_email)
            request.session['logged_user_id'] = logged_user.id
            return redirect('/welcome')
        else :
            return render(request, 'login.html',
                  {'form':form})
    else:
        form = LoginForm()
        return render(request, 'login.html',
                  {'form':form})
        
def register(request):
    if len(request.GET) > 0 and 'profileType' in request.GET :
        studentForm     = StudentProfileForm(prefix="st")
        employeeForm    = EmployeeProfilForm(prefix="em") 
        if request.GET['profileType'] == 'student' :
            studentForm = StudentProfileForm(request.GET, prefix="st")
            if studentForm.is_valid():
                studentForm.save()
                return redirect('/login')
        elif request.GET['profileType'] == 'employee':
            employeeForm = EmployeeProfilForm(request.GET, prefix="em")
            if employeeForm.is_valid():
                employeeForm.save()
                return redirect('/login')
        return render(request, 'user_profile.html', {'studentForm': studentForm,
                                                     'employeeForm': employeeForm})
        
    else :
        studentForm = StudentProfileForm(prefix='st')
        employeeForm = EmployeeProfilForm(prefix="em")
        return render(request, 'user_profile.html',
                      {'studentForm':studentForm,
                       'employeeForm': employeeForm})
        