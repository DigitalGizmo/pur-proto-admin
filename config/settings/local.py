from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

STATIC_ROOT = BASE_DIR.parent / 'pur-static'
MEDIA_ROOT = BASE_DIR.parent / 'pur-media'

# STATIC_ROOT = BASE_DIR.parent.parent / 'pur-proto' / 'static'
# MEDIA_ROOT = BASE_DIR.parent.parent / 'pur-proto' / 'media'

