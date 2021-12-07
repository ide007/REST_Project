import os
import json
from django.core.management.base import BaseCommand
from rest.usersapp.models import User


JSON_PATH = 'usersapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='utf8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('users')

        User.objects.all().delete()
        for user in users:
            new_user = User(**user)
            new_user.save()
            print('user created')
