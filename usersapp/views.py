"""Вьюшка для просмотра списка пользователя, конкретного юзера и
    редактирование конкретного юзера. Нельзя удалять и добавять.
    Вывод: JSON и API."""
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.views import APIView
# from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .serializers import UserSerializer
from .models import User


class UserViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


class UserModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserAPIView(ListModelMixin, RetrieveModelMixin, GenericAPIView):
#     renderer_classes = [JSONRenderer]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request, *args, **kwargs):
#         if 'pk' in kwargs:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

# class UserAPIView(APIView):
#     renderer_classes = [JSONRenderer]
#
#     def get(self, request):
#         task = User.objects.get(pk=2)
#         serializer = UserSerializer(task)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def user_view(request):
#     task = User.objects.get(pk=2)
#     serializer = UserSerializer(task)
#     return Response(serializer.data)


# def get_view(request):
#     user = User.objects.get(pk=2)
#     serializer = UserSerializer(user)
#     render = JSONRenderer()
#     json_data = render.render(serializer.data)
#     return HttpResponse(json_data)
#
#
# @csrf_exempt
# def post_view(request):
#
#
#     pass
