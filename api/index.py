import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "physicsTimeDilation.settings")

app = get_wsgi_application()

def handler(request, response):
    return app(request, response)
