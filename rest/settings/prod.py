from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rest',
        'USER': 'admin',
        'PASSWORD': 'admin54321',
        'HOST': 'db',
        'PORT': '5432',
    }
}
