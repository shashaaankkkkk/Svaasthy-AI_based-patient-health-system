# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class chart1(models.Model):
    temperature = models.FloatField(default=0)
    release_date1 = models.DateField()

    

class chart2(models.Model):
    percentage = models.CharField(max_length=255)
    pulse = models.FloatField(default=0)
    release_date2 = models.DateField()

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Department = models.CharField(max_length=50 ,default="OPD")
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)