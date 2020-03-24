from django.contrib import admin
from.models import EmployeDetails

# Register your models here.
class EmployeFields(admin.ModelAdmin):
    list_display=["ename","email","esalary"]
admin.site.register(EmployeDetails,EmployeFields)
