from django.db import models
from usersapp.models import User


class WorkProject(models.Model):
    name = models.CharField(max_length=64)
    project_id = models.PositiveIntegerField()
    project_user = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class TaskBoard(models.Model):
    project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.RESTRICT)
    task_title = models.CharField(max_length=64)
    task_description = models.TextField()
    task_status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
