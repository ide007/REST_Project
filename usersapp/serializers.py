from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework.serializers import Serializer, CharField, EmailField, BooleanField, IntegerField


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'user_name', 'first_name', 'last_name', 'email']


class UserSerializerV2(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', 'user_name', 'first_name', 'last_name', 'email']


# class UserSerializer(Serializer):
#     id = IntegerField()
#     user_name = CharField(max_length=32)
#     first_name = CharField(max_length=32, )
#     last_name = CharField(max_length=32)
#     email = EmailField()
#     is_active = BooleanField()
