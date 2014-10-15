# -*- coding: utf-8 -*-
from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.department_name

class User(models.Model):
    username = models.CharField(max_length=10)            
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department)
    
        
    def __unicode__(self):
        return self.full_name
    
class Computer(models.Model):
    COMP_TYPE_CHOICES = (
        ('D', 'Desktop'),
        ('L', 'Laptop'),
    )
    inum = models.IntegerField()
    comp_name = models.CharField(max_length=15)
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    comp_type = models.CharField(max_length=1, choices=COMP_TYPE_CHOICES)
    os = models.CharField(max_length=100)
    department = models.ForeignKey(Department)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.comp_name
        
class Monitor(models.Model):  
    inum = models.IntegerField()
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    department = models.ForeignKey(Department)
    user = models.ForeignKey(User)
    

        
    def __unicode__(self):
        result = str(self.model) + '_'  + str(self.inum)
        return result
        
class Ups(models.Model):
    inum = models.IntegerField()
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    department = models.ForeignKey(Department)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        result = str(self.model) + '_'  + str(self.inum)
        return result
        
class MenuItem(models.Model):
    order_id = models.IntegerField()
    item = models.CharField(max_length=30)
    link = models.CharField(max_length=200)
    
 