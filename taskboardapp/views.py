# from django.http import HttpResponse
# from rest_framework.decorators import renderer_classes
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from taskboardapp.models import WorkProject, TaskBoard
from taskboardapp.serializers import WorkProjectSerializer, TaskBoardSerializer


class WorkProjectViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = WorkProject.objects.all()
    serializer_class = WorkProjectSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


# class WorkProjectParamFilterViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = WorkProject.objects.all()
#     serializer_class = WorkProjectSerializer
#
#     def get_queryset(self):
#         name = self.request.query_params.get('name', '')
#         projects = WorkProject.objects.all()
#         if name:
#             projects = projects.filter(name__contains=name)
#         return projects
    # def get_queryset(self, name=None):
    #     return WorkProject.objects.filter(name=self.request.query_params.get(name))

# class WorkProjectViewSet(ModelViewSet):
#     queryset = WorkProject.objects.all()
#     serializer_class = WorkProjectSerializer


class TaskBoardViewSet(ListModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = TaskBoard.objects.all()
    serializer_class = TaskBoardSerializer

# class TaskBoardViewSet(ModelViewSet):
#     queryset = TaskBoard.objects.all()
#     serializer_class = TaskBoardSerializer
