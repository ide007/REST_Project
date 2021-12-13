from rest_framework.serializers import ModelSerializer
from usersapp.serializers import UserSerializer
from .models import WorkProject, TaskBoard


class WorkProjectSerializer(ModelSerializer):
    class Meta:
        model = WorkProject
        fields = '__all__'


class TaskBoardSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TaskBoard
        fields = '__all__'
