from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from .serializers import UserSerializer
from .models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def get_view(request):
    user = User.objects.get(pk=2)
    serializer = UserSerializer(user)
    render = JSONRenderer()
    json_data = render.render(serializer.data)
    return HttpResponse(json_data)


@csrf_exempt
def post_view(request):


    pass
