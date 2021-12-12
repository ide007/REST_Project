from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'first_name', 'last_name', 'email']
