# -*- coding: utf-8 -*-
"""
Created on Sat May 31 17:17:47 2014

@author: anton
"""
from equipment.models import Department
from django.template import Library
register = Library()

@register.inclusion_tag('base_menu.html')
def important_function():
    menu_list = Department.objects.order_by('department_name')
    
    return {'menu_list1':menu_list}