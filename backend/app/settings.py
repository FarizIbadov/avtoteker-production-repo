import os
from pathlib import Path
import logging

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET", "j56@jyc()*qnyl1vj^yf5_a5c27kfp5ysf^yeoxl#ul4hn^j^(")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "1") == '1'

ALLOWED_HOSTS =  ['172.20.10.4', '192.168.0.164', '192.168.0.152','localhost'] if DEBUG else os.environ.get("ALLOWED_HOSTS","").split(",")

 
if DEBUG:
    CORS_ALLOWED_ORIGINS = ['http://localhost:3000','http://localhost:8000']
else:
    CORS_TRUSTED_ORIGINS = ALLOWED_HOSTS.copy()

# Application definition

INSTALLED_APPS = [
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',
    'django.contrib.sitemaps',

    "ckeditor",
    'ckeditor_uploader',
    "rest_framework",
    "colorfield",
    "corsheaders",
    "django_cleanup.apps.CleanupConfig",
    "crispy_forms",
    "import_export",
    'rosetta',

    "social.apps.SocialConfig",
    "ordering.apps.OrderingConfig",
    "tireapp.apps.TireappConfig",
    "specific.apps.SpecificConfig",
    "main_site.apps.MainSiteConfig",
    "wheel_size.apps.WheelSizeConfig",
    "faviconapp.apps.FaviconappConfig",
    "metaapp.apps.MetaappConfig",
    "oilapp.apps.OilappConfig",
    "campaign",
    "news",
    'navigation',
    "kredit",
    "kredit_taksit",
    "sticker",
    "emailapp",
    "secure_sites",
    "adv",
    "adds.apps.AddsConfig",
    "copyright.apps.CopyrightConfig",
    # "waranty"
    # "about_us"
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

SITE_ID = 1

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Advance',
        "width": "100%"
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_DB", "avtoteker"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"), 
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "3151936f"),
        "HOST": "localhost" if DEBUG else "db",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "az"

LANGUAGES = (
    ('az', _("Azerbaijani")),
    ('en', _("English")),
    ('ru', _("Russian")),
    ('tr', _("Turkey")),
)

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_ROOT = "/vol/web/static"

MEDIA_ROOT =  os.path.join(BASE_DIR,"media") if DEBUG else '/vol/web/media'
STATIC_URL = "/static/" if DEBUG else '/static/static/'
MEDIA_URL = "/media/" if DEBUG else '/static/media/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

CRISPY_TEMPLATE_PACK = "bootstrap4"
IMPORT_EXPORT_USE_TRANSACTIONS = True
CKEDITOR_UPLOAD_PATH = "ck_uploads"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

LOCALE_PATHS = (
    BASE_DIR / 'locale',
)

MODELTRANSLATION_DEFAULT_LANGUAGE = "az"

ROSETTA_WSGI_AUTO_RELOAD = True
ROSETTA_UWSGI_AUTO_RELOAD = ROSETTA_WSGI_AUTO_RELOAD

# LOGGING = None

# if not DEBUG:
#     LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': False,
#         'handlers': {
#             'console': {
#                 'class': 'logging.StreamHandler',
#             },
#         },
#         'loggers': {
#             'django': {
#                 'handlers': ['console'],
#                 'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#             },
#         },
#     }

