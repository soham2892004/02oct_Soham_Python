from django.contrib import admin
from dbApp.models  import EmployeeTab
# Register your models here.

class Employeeadmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_Description')
    
admin.site.register(EmployeeTab,Employeeadmin)