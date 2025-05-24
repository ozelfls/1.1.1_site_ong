import os
import django
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
from django.views.decorators.csrf import csrf_exempt
from django.template import engines
from django.conf.urls.static import static

# Diretórios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..'))

TEMPLATES_DIR = os.path.join(PROJECT_ROOT, 'templates')
STATIC_DIR = os.path.join(PROJECT_ROOT, 'static')

# Configuração Django
settings.configure(
    DEBUG=True,
    SECRET_KEY='private',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
    ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [TEMPLATES_DIR],
            'APP_DIRS': False,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                ],
            },
        },
    ],
    STATIC_URL='/static/',
    STATICFILES_DIRS=[STATIC_DIR],
)

django.setup()

# Template engine
django_engine = engines['django']

# Views
def index(request):
    template = django_engine.get_template('index.html')
    return HttpResponse(template.render({}, request))

def sobre(request):
    template = django_engine.get_template('about.html')
    return HttpResponse(template.render({}, request))

def unidade(request):
    template = django_engine.get_template('unidade.html')
    return HttpResponse(template.render({}, request))

@csrf_exempt
def receber_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            print("Email recebido:", email)
            return HttpResponse('<h1>Email recebido com sucesso!</h1>')
        return HttpResponse('<h1>Email não fornecido!</h1>', status=400)
    return HttpResponse('<h1>Envie via POST!</h1>', status=405)

def formulario(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Formulário de Email</title>
        <link rel="stylesheet" href="/static/styles.css">
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

# URLs
urlpatterns = [
    path('', index),
    path('inicio/',index),
    path('sobre/', sobre),
    path('unidade/', unidade),
    path('formulario/', formulario),
    path('enviar/', receber_email),
]

# Serve arquivos estáticos durante o DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=STATIC_DIR)

# Rodar servidor
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
    execute_from_command_line(["manage.py", "runserver"])
