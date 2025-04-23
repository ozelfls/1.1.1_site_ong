import os
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

django.setup()

#esse pedaço recebe e valida o formulario com feedbaks de erros 
@csrf_exempt
def receber_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            print("Email recebido:", email)
            return HttpResponse('Email recebido com sucesso!')
        return HttpResponse('Email não fornecido!', status=400)
    return HttpResponse('Envie por POST!', status=405)

# esse pedaço mostra o formulario enviado 
def formulario(request):
    template = loader.get_template('formulario.html')
    return HttpResponse(template.render())

urlpatterns = [ # rota para o mondongo db que não ta funcionando 
    path('', formulario),
    path('enviar/', receber_email),
]

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
    execute_from_command_line(["manage.py", "runserver"])





