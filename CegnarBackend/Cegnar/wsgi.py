"""
WSGI config for Cegnar project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cegnar.settings.dev")

# application = get_wsgi_application()


def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"Hello World"]
