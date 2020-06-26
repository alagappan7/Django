from django.conf import settings
from django.db import migrations,models
from django import forms

DEPT_CHOICES = (
    ('cse','CSE'),
    ('ece', 'ECE'),
    ('it','IT'),
    ('mech','MECH'),
    ('civil','CIVIL'),
)

class techque(models.Model):
    question=models.TextField(max_length=250,blank=True,null=True)
    quetype=models.CharField(max_length=100,blank=True,null=True)
    response=models.TextField(max_length=250,blank=True,null=True)  
    sample1=models.TextField(max_length=250,blank=True,null=True)  
    sample2=models.TextField(max_length=250,blank=True,null=True)  
    sample3=models.TextField(max_length=250,blank=True,null=True)  


class commque(models.Model):
    question=models.TextField(max_length=250,blank=True,null=True)
    quetype=models.CharField(max_length=100,blank=True,null=True)  
    response=models.TextField(max_length=250,blank=True,null=True)  

class Users(models.Model): 
    name = models.CharField(max_length=200,blank=True,null=True)
    Fathername = models.CharField(max_length=200,blank=True,null=True)
    collegeid = models.CharField(max_length=200,blank=True,null=True)
    collegename = models.CharField(max_length=200,blank=True,null=True)
    #color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    Department = models.CharField(max_length=70,choices=DEPT_CHOICES,default='cse')
    mailid=models.EmailField(max_length = 254,blank=True,null=True)
    writeuperrors=models.IntegerField(blank=True,null=True)
    text=models.TextField(max_length=250,blank=True,null=True)
    progscore=models.IntegerField(blank=True,null=True)
    networkscore=models.IntegerField(blank=True,null=True)
    oopsscore=models.IntegerField(blank=True,null=True)