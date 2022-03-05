import os
from pathlib import Path
from configurations import Configuration
from dotenv import load_dotenv, find_dotenv


class BaseConfig(Configuration):
    load_dotenv(find_dotenv())
    BASE_DIR = Path(__file__).parent.parent
    SECRET_KEY = os.environ['SECRET_KEY']
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.contenttypes',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'api',
        'rest_framework',
        'simple_history',
    ]

    MIDDLEWARE = [
        'django.middleware.common.CommonMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'project.urls'

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

    WSGI_APPLICATION = 'project.wsgi.application'
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'America/Sao_Paulo'
    USE_I18N = True
    USE_L10N = True

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 200,
        'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
    }

    APPEND_SLASH = True

    SIMPLE_HISTORY_HISTORY_ID_USE_UUID = True

    GRAPHENE = {
        'SCHEMA': 'project.schema.schema'
    }


class Dev(BaseConfig):
    ALLOWED_HOSTS = ['*']
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'OPTIONS': {
                'options': '-c search_path=app_finance'
            },
            'NAME': os.environ['DEV_DB_FIN_NAME'],
            'USER': os.environ['DEV_DB_FIN_USER'],
            'PASSWORD': os.environ['DEV_DB_FIN_PASS'],
            'HOST': os.environ['DEV_DB_FIN_HOST'],
            'PORT': 5432,
        }
    }
    STATIC_URL = '/static/'

class Stage(BaseConfig):
    ALLOWED_HOSTS = ['*']
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'OPTIONS': {
                'options': '-c search_path=app_finance'
            },
            'NAME': os.environ['STA_DB_FIN_NAME'],
            'USER': os.environ['STA_DB_FIN_USER'],
            'PASSWORD': os.environ['STA_DB_FIN_PASS'],
            'HOST': os.environ['STA_DB_FIN_HOST'],
            'PORT': 5432,
        }
    }
    STATIC_URL = '/static/'