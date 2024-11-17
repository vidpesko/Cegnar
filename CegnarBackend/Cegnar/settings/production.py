import os
from dotenv import load_dotenv

from .base import *


# Load environment variables from .env file
load_dotenv()

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [".cegnarblacksmithing.com"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "public_html")
STATIC_ROOT = os.path.join(PARENT_DIR, "static")
MEDIA_ROOT = os.path.join(PARENT_DIR, "media")

WAGTAILADMIN_BASE_URL = "https://cegnarblacksmithing.com"


try:
    from .local import *
except ImportError:
    pass
