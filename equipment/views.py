from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

from equipment.models import Computer, Department, Monitor, Ups, User, MenuItem



def index(request):
    departments_list = Department.objects.order_by('department_name')
    menu_items = MenuItem.objects.order_by('order_id')
    context = {'departments_list': departments_list, 'menu_items':menu_items}
    context['menu_list'] = menu()
    return render(request, 'equipment/index.html', context)

    
def computer(request, computer_inum):
    computer = get_object_or_404(Computer, inum=computer_inum)
    return render(request, 'equipment/computers/computer.html', {'computer':computer})
    

def computers(request):
    computers_list = Computer.objects.order_by('comp_name')
    context = {'computers_list': computers_list}
    return render(request, 'equipment/computers/index.html', context)

def departments(request):
    departments_list = Department.objects.order_by('department_name')
    context = {'departments_list':departments_list}
    return render(request, 'equipment/departments/index.html', context)

def department(request, department):
    comp_id = Department.objects.get(department_name=department)
    computers_list = Computer.objects.filter(department=comp_id)
    monitors_list = Monitor.objects.filter(department=comp_id)
    upses_list = Ups.objects.filter(department=comp_id)
#    equipment_list = [computers_list, monitors_list, upses_list]
    department_name = department
    context = {'computers_list':computers_list, 'monitors_list':monitors_list, 'upses_list':upses_list, 'department_name':department_name }
#    context = {'equipment_list':equipment_list, 'department_name':department_name }
    return render(request,'equipment/departments/department.html', context)

def user(request, user):
    user_id = User.objects.get(full_name=user)
    computers_list = Computer.objects.filter(user=user_id)
    monitors_list = Monitor.objects.filter(user=user_id)
    upses_list = Ups.objects.filter(user=user_id)
    username = user
    context = {'computers_list':computers_list, 'monitors_list':monitors_list, 'upses_list':upses_list, 'username':username}
    return render(request, 'equipment/users/user.html', context)
    return HttpResponse("You're watching %s page" % user)

def monitor(request, monitor_inum):
    monitor = get_object_or_404(Monitor, inum=monitor_inum)
    return render(request, 'equipment/monitors/monitor.html', {'monitor':monitor})
    
def ups(request, ups_inum):
    ups = get_object_or_404(Ups, inum=ups_inum)
    return render(request, 'equipment/upses/ups.html', {'ups':ups})
    
def menu():
    return Department.objects.order_by('department_name')
