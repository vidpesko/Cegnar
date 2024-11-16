from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5+8kim@j*r^0f=rwe(rt@dmb1h($=lii=r$bpmh5rzwy5qjnw)"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [".cegnarblacksmithing.com"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "public_html")
STATIC_ROOT = os.path.join(PARENT_DIR, "static")
MEDIA_ROOT = os.path.join(PARENT_DIR, "media")


try:
    from .local import *
except ImportError:
    pass
