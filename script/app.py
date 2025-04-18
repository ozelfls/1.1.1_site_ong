'''import os
import django
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
from django.views.decorators.csrf import csrf_exempt

settings.configure(
    DEBUG = True,
    ROOT_URLCONF = __name__,
    SECRET_KEY =' private e-mail porra',
    ALLOWED_HOSTS = ['*'],
    MIDDLEWARE = [
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
    ],
)
''' 

# nota mental de terminar depois essa feature de private 



