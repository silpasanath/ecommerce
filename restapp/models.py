from django.db import models
from rest_framework import serializers
# Create your models here.

def func(value):
    if (value=='hello'):
        return value
    else:
        raise serializers.ValidationError("the taskname should be hello")

def func1(value):
    if value.isalpha():
        return value
    else:
        raise serializers.ValidationError("the user should be alpabets")

class todos(models.Model):
    taskname=models.CharField(max_length=50,validators=[func])
    user=models.CharField(max_length=50,validators=[func1])
    is_active=models.BooleanField(default=True)
    date=models.DateField(auto_now_add=True)  #24/10/23 +timedelta(100)

class moviemodel(models.Model):
    moviename=models.CharField(max_length=50)
    releaseddate=models.DateField()
    characters=models.CharField(max_length=50)
    theatrename=models.CharField(max_length=50)
    directorname=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)

class hotelmodel(models.Model):
    hotelname=models.CharField(max_length=50)
    bookingdate=models.DateField()
    hotelimage=models.ImageField()
    rating=models.FloatField()
    location=models.CharField(max_length=50)
    number=models.IntegerField()

class productmodel(models.Model):
    product_name=models.CharField(max_length=50)
    price=models.IntegerField()
    added_date=models.DateField(auto_now_add=True)

class fileupmodel(models.Model):
    pdf=models.FileField(upload_to='pdf/')
    audiofile=models.FileField(upload_to='audio/')
    videofile=models.FileField(upload_to='video/')

class filesupmodel(models.Model):
    pdf=models.FileField(upload_to='pdf/')
    audiofile=models.FileField(upload_to='audio/')
    videofile=models.FileField(upload_to='video/')

class viewmodel(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()

class studentmodel(models.Model):
    student_name=models.CharField(max_length=50)
    dob=models.DateField()
    gender=models.CharField(max_length=50)
    student_image=models.FileField()
    phone=models.IntegerField()

class personmodel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.IntegerField()

#API creaton using fun
class employeemodel(models.Model):
    employee_name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    number=models.IntegerField()

#API using unauthenticated user

class userregmodel(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()


#validators

def unamefun(value):
    if value.isalpha():
        return value
    else:
        raise serializers.ValidationError["enter valid name"]

def productname(value):
    if value.isalnum():
        return value
    else:
        raise serializers.ValidationError("special characters not allowed")

import datetime

def datefun(value):
    deldate=datetime.date.today()
    if value<=deldate:
        return value
    else:
        raise serializers.ValidationError("must be below the current date")


class customermodel(models.Model):
    name=models.CharField(max_length=10,validators=[unamefun])
    product_name=models.CharField(max_length=100,validators=[productname])
    delivered_date=models.DateField(validators=[datefun])

