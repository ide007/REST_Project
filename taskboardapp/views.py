from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from taskboardapp.models import WorkProject, TaskBoard
from taskboardapp.serializers import WorkProjectSerializer, TaskBoardSerializer


class WorkProjectViewSet(ModelViewSet):
    queryset = WorkProject.objects.all()
    serializer_class = WorkProjectSerializer


class TaskBoardViewSet(ModelViewSet):
    queryset = TaskBoard.objects.all()
    serializer_class = TaskBoardSerializer
