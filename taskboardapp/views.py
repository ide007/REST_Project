from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from taskboardapp.models import WorkProject, TaskBoard
from taskboardapp.serializers import WorkProjectSerializer, TaskBoardSerializer
from .filters import WorkProjectFilter


# class ProjectPagination(LimitOffsetPagination):
#     default_limit = 10


class WorkProjectViewSet(ListModelMixin,
                         RetrieveModelMixin,
                         UpdateModelMixin,
                         CreateModelMixin,
                         DestroyModelMixin,
                         GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = WorkProject.objects.all()
    serializer_class = WorkProjectSerializer
    filterset_class = WorkProjectFilter
    # pagination_class = ProjectPagination


class TaskBoardViewSet(ListModelMixin,
                         RetrieveModelMixin,
                         UpdateModelMixin,
                         CreateModelMixin,
                         DestroyModelMixin,
                         GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = TaskBoard.objects.all()
    serializer_class = TaskBoardSerializer
    filterset_fields = ['project']
    # pagination_class = ProjectPagination

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        task.task_status = False
        task.is_deleted = True
        task.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
