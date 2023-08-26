# check_data.py
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employees.settings')  # your_project_nameを実際のプロジェクト名に置き換えてください
django.setup()

from api.models import Department, Employee, Project, EmployeeProjectAssignment  # app_nameを実際のアプリ名に置き換えてください

# 部署データの確認
print("---- 部署データ ----")
departments = Department.objects.all()
for dept in departments:
    print(dept.name, dept.location)

# 社員データの確認
print("\n---- 社員データ ----")
employees = Employee.objects.all()
for emp in employees:
    print(emp.name, emp.email, emp.job_title, emp.department.name)

# プロジェクトデータの確認
print("\n---- プロジェクトデータ ----")
projects = Project.objects.all()
for proj in projects:
    print(proj.name, proj.start_date, proj.end_date)

# 社員プロジェクトアサインデータの確認
print("\n---- 社員プロジェクトアサインデータ ----")
assignments = EmployeeProjectAssignment.objects.all()
for assign in assignments:
    print(assign.employee.name, assign.project.name, assign.assign_date, assign.role)

