"""
Django settings for spayde project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT=os.path.join(BASE_DIR,'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c)kh^hy+qz0v=)+xo8gp=+p_a#2@t5k9fbiru03=620+pcx!@j'

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
    'myapp','cloudinary',
    'cloudinary_storage',
    'whitenoise',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spayde.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'template'],
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

WSGI_APPLICATION = 'spayde.wsgi.application'

import cloudinary
import cloudinary.uploader
import cloudinary.api

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'dwyxrrxvw',
#     'API_KEY': '627336925288547',
#     'API_SECRET': 'cJ1yuEAmq2KzKNSsdmffZuwrB88',
# }

import cloudinary

cloudinary.config(  
    cloud_name="dwyxrrxvw",  
    api_key="627336925288547",  
    api_secret="cJ1yuEAmq2KzKNSsdmffZuwrB88"  
)

import cloudinary
import os

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME", "dwyxrrxvw"),
    api_key=os.getenv("CLOUDINARY_API_KEY", "627336925288547"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET", "cJ1yuEAmq2KzKNSsdmffZuwrB88"),
)


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CSRF_TRUSTED_ORIGINS = ["https://res.cloudinary.com"]


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'railway',
        'USER': 'root',
        'PASSWORD': 'UYeSBlkNVyTlWoqDppicbikAZgAUAzND',
        'HOST': 'shuttle.proxy.rlwy.net',
        'PORT': '25362',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL='media/'

STATICFILES_DIRS = [BASE_DIR/'static']

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
