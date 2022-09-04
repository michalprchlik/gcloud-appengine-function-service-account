
from settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
USER_LOGIN_URL = "login"

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}