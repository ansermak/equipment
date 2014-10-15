from django.contrib import admin
from equipment.models import Department, User, Computer, Monitor, Ups, MenuItem
from django.forms import ModelForm
from django.forms.models import ModelChoiceField

class ComputerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['comp_name', 'comp_type']}),
        ('Info', {'fields':['inum', 'serial_number', 'model', 'os']}),
        ('Department/User', {'fields':['department', 'user']})
    ]
    list_display = ('comp_name', 'department', 'user')
    search_fields=['comp_name']
    
class MonitorAdminForm(ModelForm):
    class Meta:
        model = Monitor
        
    def __init__(self,*args, **kwargs):
        super(MonitorAdminForm, self).__init__(*args, **kwargs)
        instance = kwargs.pop('instance', None)
        if instance:
            self.fields['user'].queryset = User.objects.filter(department=instance.department)


    
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('model', 'inum', 'department', 'user')    
    fieldsets = [
        ('Info', {'fields':['inum', 'serial_number', 'model']}),
        ('Department/User', {'fields':['department', 'user']})
    ] 

#    form = MonitorAdminForm
    
class UpsAdmin(admin.ModelAdmin):
    list_display = ('model', 'inum', 'department', 'user')
    fieldsets = [
        ('Info', {'fields':['inum', 'serial_number', 'model']}),
        ('Department/User', {'fields':['department', 'user']})
    ]
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'department')
    search_fields=['username', 'full_name']
   
class MenuItemAdmin(admin.ModelAdmin):
     list_display = ('item', 'link', 'order_id')
    

admin.site.register(Computer, ComputerAdmin)
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Ups, UpsAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(MenuItem, MenuItemAdmin)

