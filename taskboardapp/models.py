from django.db import models
from usersapp.models import User


class WorkProject(models.Model):
    name = models.CharField(verbose_name='Название проекта', max_length=64)
    repository_link = models.URLField(verbose_name='ссылка на проект', null=True)
    project_id = models.AutoField(primary_key=True)
    project_user = models.ManyToManyField(User, verbose_name='Участники')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class TaskBoard(models.Model):
    project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.RESTRICT)
    task_title = models.CharField(max_length=64)
    task_description = models.TextField()
    task_status = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
