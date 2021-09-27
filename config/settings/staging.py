from .base import *

DEBUG = True

ALLOWED_HOSTS = ['admin.picturingurbanrenewal.org', 
    '142.93.1.173', '127.0.0.1', 'localhost']

STATIC_ROOT = BASE_DIR.parent.parent / 'pur-proto' / 'static'

MEDIA_ROOT = BASE_DIR.parent.parent / 'pur-proto' / 'media'

