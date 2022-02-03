from rest_framework.serializers import ModelSerializer
from .models import WorkProject, TaskBoard


class WorkProjectSerializer(ModelSerializer):
    class Meta:
        model = WorkProject
        fields = ['project_id', 'name', 'repository_link', 'project_user']


class TaskBoardSerializer(ModelSerializer):

    class Meta:
        model = TaskBoard
        fields = ['id', 'task_title', 'task_status', 'project', 'creator',
                  'created_time', 'is_deleted']
        # fields = '__all__'
