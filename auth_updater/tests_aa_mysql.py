from ..allianceauth.tests.settings_all import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'alliance_auth',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'OPTIONS': {'charset': 'utf8mb4'},
}
