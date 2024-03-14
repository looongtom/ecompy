"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8@=d47!t*9hj+#1r*(!5=wd#=f5(62g9g4!d)vi2fy=^b82w24'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'person.apps.PersonConfig',
    'book.apps.BookConfig',
    'cart.apps.CartConfig',
    'catalog.apps.CatalogConfig',
    'mobile.apps.MobileConfig',
    'clothe.apps.ClotheConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'person_project.urls'

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

WSGI_APPLICATION = 'person_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
 'default': {
        'ENGINE': 'djongo',
        'NAME': 'ecommerce',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb://tom:123456@172.18.80.121:2717/ecommerce'
        }
    },

# 'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'ecomstore',
#         'USER': 'root',
#         'PASSWORD': 'tr1nhtu@n',
#         'HOST':'localhost',
#         'PORT':'3306',
#     }
    'book': {
        'ENGINE': 'djongo',
        'NAME': 'ecommerce',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb://tom:123456@172.18.80.121:2717/ecommerce'
        }
    },
    'category': {
        'ENGINE': 'djongo',
        'NAME': 'ecommerce',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb://tom:123456@172.18.80.121:2717/ecommerce'
        }
    },
    'cart': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecomstore',
        'USER': 'root',
        'PASSWORD': 'tr1nhtu@n',
        'HOST':'localhost',
        'PORT':'3306',
    },
    'catalog': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecomstore',
        'USER': 'root',
        'PASSWORD': 'tr1nhtu@n',
        'HOST':'localhost',
        'PORT':'3306',
    },
    'clothe': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecomstore',
        'USER': 'root',
        'PASSWORD': 'tr1nhtu@n',
        'HOST':'localhost',
        'PORT':'3306',
    },
    'mobile': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecomstore',
        'USER': 'root',
        'PASSWORD': 'tr1nhtu@n',
        'HOST':'localhost',
        'PORT':'3306',
    },
    'person': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecomstore',
        'USER': 'root',
        'PASSWORD': 'tr1nhtu@n',
        'HOST':'localhost',
        'PORT':'3306',
    },
}

DATABASE_ROUTERS = [
    'person_project.database_router.PersonRouter',
    'person_project.database_router.BookRouter',
    'person_project.database_router.CartRouter',
    'person_project.database_router.CatalogRouter',
    'person_project.database_router.MobileRouter',
    'person_project.database_router.ClotheRouter',
    'person_project.database_router.CategoryRouter',
]


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_URL = 'static/'
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # new

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(CURRENT_PATH, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
