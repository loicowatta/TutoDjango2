#-*- coding: utf-8 -*-
'''
Created on 24 févr. 2018

@author: loico
'''
from django.db import models

class Person(models.Model):
    person_type = 'generic'
    def __str__(self):
        return self.first_name + " " + self.last_name
    registration_number = models.CharField(max_length=10)
    last_name           = models.CharField(max_length=30)
    first_name          = models.CharField(max_length=30)
    birth_date          = models.DateField()
    email               = models.EmailField()
    home_phone          = models.CharField(max_length=20)
    cellphone           = models.CharField(max_length=20)
    password            = models.CharField(max_length=32)
    friends = models.ManyToManyField('self')
    falculty = models.ForeignKey('Faculty',default=None, on_delete=None, null=True)
    
class Message(models.Model):
    def __str__(self):
        return self.content[:19]+"..."
    author = models.ForeignKey('Person', on_delete=None, null=True)
    content = models.TextField()
    publication_date = models.DateField()
    
class Faculty(models.Model):
    def __str__(self):
        return self.name
    name    = models.CharField(max_length=30)
    color   = models.CharField(max_length=6)
    
class Campus(models.Model):
    def __str__(self):
        return self.name
    name    = models.CharField(max_length=30)
    address   = models.CharField(max_length=60)
    
class Job(models.Model):
    def __str__(self):
        return self.title
    title    = models.CharField(max_length=30)
    
class Cursus(models.Model):
    def __str__(self):
        return self.title
    title    = models.CharField(max_length=30)
    
class Employee(Person):
    person_type = 'employee'
    office  = models.CharField(max_length=30)
    campus  = models.ForeignKey('Campus', on_delete=None, null=True)
    job     = models.ForeignKey('Job', on_delete=None, null=True)
    
class Student(Person):
    person_type = 'student'
    cursus  = models.ForeignKey('Cursus', on_delete=None, null=True)
    year    = models.BigIntegerField()
    
    