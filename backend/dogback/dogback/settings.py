"""
Django settings for dogback project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import datetime
import os
import json
import sys
import my_settings
from django.core.exceptions import ImproperlyConfigured
# import pymysql
# pymysql.install_as_MYSQLdb()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# APPEND_SLASH=False


####-key값 분리
# ROOT_DIR = os.path.dirname(BASE_DIR)
# SECRET_BASE_FILE = os.path.join(BASE_DIR, 'secrets.json')

# secrets = json.loads(open(SECRET_BASE_FILE).read())
# for key, value in secrets.items():
#     setattr(sys.modules[__name__],key,value)
####-key값 분리

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-0n!*vkk8wb0yls7@6e)+m-h6m%6$zl_kob22i1yzg#+7zmi)^3'
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file, 'r') as f:
    secrets = json.loads(f.read())
def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)
SECRET_KEY = get_secret("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['192.168.0.1']
#ALLOWED_HOSTS = ['220.120.192.122'] # setting React Native

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'corsheaders',

    'allauth.socialaccount',
    'dogaccount',
    'animal_hospital',
    'diary',
    'yolov05',
    
]
SITE_ID = 1
#AUTH_USER_MODEL = 'accounts.User'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# rest-auth 로그인할때 username 빼고 email로만 회원가입 하게 하는 setting
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_SESSION_REMEMBER = True
SESSION_COOKIE_AGE = 3600
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True   
ACCOUNT_USERNAME_REQUIRED = False
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True


AUTHENTICATION_BACKENDS = (
 "django.contrib.auth.backends.ModelBackend",
 "allauth.account.auth_backends.AuthenticationBackend",
)
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        #Authentication을 모든 view에서 동일하게 사용하는 setting
        'rest_framework.authentication.BasicAuthentication', 
        'rest_framework.authentication.SessionAuthentication', # 실제 돌릴때
        #'rest_framework.authentication.TokenAuthentication', # Postman에서 돌릴때


    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    # 'DEFAULR_RENDERER_CLASSES' :  ('rest_framework.renerers.JSONRenderer',)
}
#### email login-------------------------------------

REST_USE_JWT = True
# DATABASES = my_settings.DATABASES
# SECRET_KEY = my_settings.SECRET_KEY
#SECRET_KEY = 'django-insecure-0n!*vkk8wb0yls7@6e)+m-h6m%6$zl_kob22i1yzg#+7zmi)^3'
#JWT 인증
JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',     
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#CORS

CORS_ORIGIN_WHITELIST = [ 'http://192.168.0.1']

CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)


ROOT_URLCONF = 'dogback.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dogback.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    #mysql3 database 연동
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

    #mysql database 연동
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'MYTEST',
    #     'USER': 'root',
    #     'PASSWORD': 'whtjdals0306!',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


