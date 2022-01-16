"""Вьюшка для просмотра списка пользователя, конкретного юзера и
    редактирование конкретного юзера. Нельзя удалять и добавять.
    Вывод: JSON и API."""
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .serializers import UserSerializer, UserSerializerV2
from .models import User
from rest_framework.permissions import DjangoModelPermissions


class UserViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    permission_classes = [DjangoModelPermissions]
    # serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserSerializerV2
        return UserSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


class UserModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer
