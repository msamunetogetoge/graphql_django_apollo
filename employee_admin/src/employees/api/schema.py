import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from .models import Department, Employee, Project, EmployeeProjectAssignment


class DepartmentNode(DjangoObjectType):
    class Meta:
        model = Department
        filter_fields = ['name', 'location']
        interfaces = (graphene.relay.Node, )


class EmployeeNode(DjangoObjectType):
    class Meta:
        model = Employee
        filter_fields = ['name', 'email', 'job_title', 'department']
        interfaces = (graphene.relay.Node, )


class ProjectNode(DjangoObjectType):
    class Meta:
        model = Project
        filter_fields = ['name', 'start_date', 'end_date']
        interfaces = (graphene.relay.Node, )


class EmployeeProjectAssignmentNode(DjangoObjectType):
    class Meta:
        model = EmployeeProjectAssignment
        filter_fields = ['employee', 'project', 'assign_date', 'role']
        interfaces = (graphene.relay.Node, )


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'job_title', 'department')

class Query(graphene.ObjectType):
    department = graphene.relay.Node.Field(DepartmentNode)
    all_departments = DjangoFilterConnectionField(DepartmentNode)

    employee = graphene.relay.Node.Field(EmployeeNode)
    all_employees = DjangoFilterConnectionField(EmployeeNode)

    project = graphene.relay.Node.Field(ProjectNode)
    all_projects = DjangoFilterConnectionField(ProjectNode)

    assignment = graphene.relay.Node.Field(EmployeeProjectAssignmentNode)
    all_assignments = DjangoFilterConnectionField(
        EmployeeProjectAssignmentNode)
    
    employees_by_department_and_project = graphene.List(
        EmployeeType,
        department_id=graphene.ID(required=True),
        project_id=graphene.ID(required=True)
    )

    def resolve_employees_by_department_and_project(self, info, department_id, project_id):
        # 部署とプロジェクトの両方に属する社員のIDを取得
        try:
            employee_ids = EmployeeProjectAssignment.objects.filter(project_id=from_global_id(project_id)[1]).values_list('employee_id', flat=True)
            
            # IDと部署を元に社員をフィルタリングし、関連するdepartmentも一緒に取得
            return Employee.objects.filter(id__in=employee_ids, department_id=from_global_id(department_id)[1]).select_related('department')
        except Exception as e:
            print(e)
            raise e
            


schema = graphene.Schema(query=Query)
