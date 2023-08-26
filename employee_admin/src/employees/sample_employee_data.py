import os
import django
# your_project_nameを実際のプロジェクト名に置き換えてください
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employees.settings')
django.setup()


from faker import Faker
from api.models import Department, Employee
import random



# your_app_nameを適切なアプリ名に置き換えてください django.seupの後にやる


fake = Faker("ja_JP")

# データベース内の部署の数を取得
num_departments = Department.objects.all().count()

for _ in range(30):
    employee = Employee(
        name=fake.name(),
        email=fake.email(),
        job_title=fake.job(),
        department=Department.objects.get(
            id=random.randint(1, num_departments))
    )
    employee.save()

employees = Employee.objects.all()
for e in employees:
    print(e)
