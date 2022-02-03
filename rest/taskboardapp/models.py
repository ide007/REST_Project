from django.db import models
from rest.usersapp.models import User


class WorkProject(models.Model):
    name = models.CharField(verbose_name='Название проекта', max_length=64)
    repository_link = models.URLField(verbose_name='ссылка на проект', null=True)
    project_id = models.AutoField(primary_key=True)
    project_user = models.ManyToManyField(User, verbose_name='Участники')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class TaskBoard(models.Model):
    project = models.ForeignKey(WorkProject, on_delete=models.CASCADE, verbose_name='Проект')
    creator = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='Ответственный')
    task_title = models.CharField(max_length=64, verbose_name='Название задачи')
    task_description = models.TextField(verbose_name='Содержание задачи')
    task_status = models.BooleanField(default=True, verbose_name='Статус задачи')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Последнее редактирование')
    is_deleted = models.BooleanField(default=False, verbose_name='Статус закрытия')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
