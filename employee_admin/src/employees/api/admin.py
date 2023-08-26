from django.contrib import admin

from .models import Department, Employee, Project, EmployeeProjectAssignment
# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(EmployeeProjectAssignment)
