from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5+8kim@j*r^0f=rwe(rt@dmb1h($=lii=r$bpmh5rzwy5qjnw)"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATIC_URL = "/py2/static/"


try:
    from .local import *
except ImportError:
    pass
