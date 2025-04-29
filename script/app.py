'''import os
import django
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
from django.views.decorators.csrf import csrf_exempt
from django.template import engines

# CONFIGURAÇÕES DJANGO
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='private',
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
    ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
        },
    ],
)

django.setup()

# PEGAR SISTEMA DE TEMPLATE
django_engine = engines['django']

# VIEW QUE RECEBE O EMAIL
@csrf_exempt
def receber_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            print("Email recebido:", email)
            return HttpResponse('<h1>Email recebido com sucesso!</h1>')
        return HttpResponse('<h1>Email não fornecido!</h1>', status=400)
    return HttpResponse('<h1>Envie via POST!</h1>', status=405)

# VIEW QUE MOSTRA O FORMULÁRIO HTML
def formulario(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Formulário de Email</title>
    </head>
    <body>
        <h1>Envie seu email</h1>
        <form method="POST" action="/enviar/">
            <input type="email" name="email" placeholder="Seu Email" required>
            <button type="submit">Enviar</button>
        </form>
    </body>
    </html>
    """
    template = django_engine.from_string(html)
    return HttpResponse(template.render())

# URLS
urlpatterns = [
    path('', formulario),
    path('enviar/', receber_email),
]

# RODAR SERVIDOR
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
    execute_from_command_line(["manage.py", "runserver"])
'''