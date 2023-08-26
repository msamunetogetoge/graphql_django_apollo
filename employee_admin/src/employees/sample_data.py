# sample_data.py
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employees.settings')  # your_project_nameを実際のプロジェクト名に置き換えてください
django.setup()

from api.models import Department, Employee, Project, EmployeeProjectAssignment  # app_nameを実際のアプリ名に置き換えてください
import datetime

# 部署データ
departments = [
    {"name": "開発部", "location": "東京"},
    {"name": "営業部", "location": "大阪"},
    {"name": "人事部", "location": "福岡"},
]

for dept in departments:
    Department.objects.create(**dept)

# 社員データ
employees = [
    {"name": "山田太郎", "email": "yamada@example.com", "job_title": "エンジニア", "department": Department.objects.get(name="開発部")},
    {"name": "鈴木花子", "email": "suzuki@example.com", "job_title": "営業", "department": Department.objects.get(name="営業部")},
    {"name": "佐藤一郎", "email": "sato@example.com", "job_title": "人事", "department": Department.objects.get(name="人事部")},
]

for emp in employees:
    Employee.objects.create(**emp)

# プロジェクトデータ
projects = [
    {"name": "プロジェクトA", "start_date": datetime.date.today(), "end_date": datetime.date.today() + datetime.timedelta(days=30)},
    {"name": "プロジェクトB", "start_date": datetime.date.today(), "end_date": datetime.date.today() + datetime.timedelta(days=60)},
]

for proj in projects:
    Project.objects.create(**proj)

# 社員プロジェクトアサインデータ
assignments = [
    {"employee": Employee.objects.get(name="山田太郎"), "project": Project.objects.get(name="プロジェクトA"), "assign_date": datetime.date.today(), "role": "リーダー"},
    {"employee": Employee.objects.get(name="鈴木花子"), "project": Project.objects.get(name="プロジェクトB"), "assign_date": datetime.date.today(), "role": "メンバー"},
]

for assign in assignments:
    EmployeeProjectAssignment.objects.create(**assign)

print("Sample data has been populated!")
