from rest_framework.serializers import ModelSerializer
from usersapp.serializers import UserSerializer
from .models import WorkProject, TaskBoard


class WorkProjectSerializer(ModelSerializer):
    class Meta:
        model = WorkProject
        fields = ['project_id', 'name', 'repository_link', 'project_user']


class TaskBoardSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TaskBoard
        # fields = ['task_title', 'task_status', 'project', 'creator', 'created_time', 'user_creator']
        fields = '__all__'
