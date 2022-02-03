from django.db import models
from django.contrib.auth.models import AbstractUser

# [Client] -> [Router/URL] -> [View] -> [Serializer] -> [Model]


class User(AbstractUser):
    user_name = models.CharField(verbose_name='Логин', max_length=32, blank=True, )
    first_name = models.CharField(verbose_name='Имя', max_length=32, )
    last_name = models.CharField(verbose_name='Фамилия', max_length=32, blank=False,)
    email = models.EmailField(unique=True, verbose_name='email', blank=True, )
    is_active = models.BooleanField(default=True,)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
