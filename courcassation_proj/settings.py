"""
Django settings for courcassation_proj project.
"""

from pathlib import Path

# -----------------------
# BASE DIRECTORIES
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# -----------------------
# SECURITY
# -----------------------
import os
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dev-key')
DEBUG = False

ALLOWED_HOSTS = [
    "courdecassation.ht",
    "www.courdecassation.ht",
]

CSRF_TRUSTED_ORIGINS = [
    "https://courdecassation.ht",
    "https://www.courdecassation.ht",
]

#ALLOWED_HOSTS = ['.onrender.com','127.0.0.1','localhost']   # mete domèn ou lè w ap deplwaye


# -----------------------
# APPS
# -----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',

    # Apps ou yo
    'arret',
]


# -----------------------
# MIDDLEWARE
# -----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # AJOUTE SA
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'courcassation_proj.urls'


# -----------------------
# TEMPLATES
# -----------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',   # folder templates global
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'courcassation_proj.wsgi.application'


# -----------------------
# DATABASE
# -----------------------
DATABASES = {
    'default': {
      #  'ENGINE': 'django.db.backends.mysql',   # MySQL engine
      #  'NAME': 'arret_db',                     # Non baz done w kreye nan MySQL
      #  'USER': 'root',                           # User MySQL ou
      #  'PASSWORD': 'root',                  # Modpas ou te mete pandan enstalasyon
      #  'HOST': '127.0.0.1',                      # Localhost
      #  'PORT': '3306',                            # Port default MySQL
      #  'OPTIONS': {
       #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
       
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
        
    




# -----------------------
# PASSWORD VALIDATION
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -----------------------
# INTERNATIONALIZATION
# -----------------------
LANGUAGE_CODE = 'fr'   # pi bon pou Haiti & Cour de cassation
TIME_ZONE = 'America/Port-au-Prince'

USE_I18N = True
USE_TZ = True


# -----------------------
# STATIC & MEDIA FILES
# -----------------------
STATIC_URL = '/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = BASE_DIR / 'staticfiles'
# -----------------------
# DJANGO DEFAULTS
# -----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

