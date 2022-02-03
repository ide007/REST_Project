import graphene
from graphene_django import DjangoObjectType
from rest.taskboardapp import TaskBoard, WorkProject
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class TaskBoardType(DjangoObjectType):
    class Meta:
        model = TaskBoard
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = WorkProject
        fields = '__all__'


class Query(graphene.ObjectType):

    all_users = graphene.List(UserType)

    all_tasks = graphene.List(TaskBoardType)

    all_projects = graphene.List(ProjectType)

    task_by_id = graphene.Field(TaskBoardType, id=graphene.Int(required=True))

    projects_by_name = graphene.Field(ProjectType, name=graphene.String(required=False))

    def resolve_task_by_id(root, info, id):
        try:
            return TaskBoard.objects.get(id=id)
        except TaskBoard.DoesNotExist:
            return None

    def resolve_projects_by_name(root, info, name=None):
        projects = ProjectType.objects.all()
        if name:
            projects = projects.filter(name__contains=name)
        return projects

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_tasks(root, info):
        return TaskBoard.objects.all()

    def resolve_all_projects(root, info):
        return WorkProject.objects.all()


schema = graphene.Schema(query=Query)
