# Generated by Django 3.2.10 on 2021-12-15 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskboardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskboard',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='taskboard',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='taskboardapp.workproject'),
        ),
    ]
