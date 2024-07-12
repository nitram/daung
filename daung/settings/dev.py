from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rs*#*%(js_jo%o_0o9&co*5s2y8_=3!rdh(i$o@jsj=g6ep!19'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

try:
    from .local import *  # noqa
except ImportError:
    pass