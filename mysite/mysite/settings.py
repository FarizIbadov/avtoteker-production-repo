import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG"), 2))
# DEBUG = True

ALLOWED_HOSTS = []
ALLOWED_HOSTS_ENV = os.environ.get("ALLOWED_HOSTS")
if DEBUG:
    ALLOWED_HOSTS.append("*")
elif ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS.extend(ALLOWED_HOSTS_ENV.split(","))


# Application definition

INSTALLED_APPS = [
    "social.apps.SocialConfig",
    "ordering.apps.OrderingConfig",
    "custom_admin.apps.CustomAdminConfig",
    "tireapp.apps.TireappConfig",
    "specific.apps.SpecificConfig",
    "main_site.apps.MainSiteConfig",
    "wheel_size.apps.WheelSizeConfig",
    "faviconapp.apps.FaviconappConfig",
    "metaapp.apps.MetaappConfig",
    "adds.apps.AddsConfig",
    "copyright.apps.CopyrightConfig",
    "django_cleanup.apps.CleanupConfig",
    "crispy_forms",
    "import_export",
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
    "oilapp.apps.OilappConfig",
    "campaign",
    "news",
    'navigation',
    "kredit"
]

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
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

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

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": "db",
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = ""
MEDIA_URL = ""


STATIC_ROOT = "/vol/web/static"
MEDIA_ROOT = ""

if DEBUG:
    MEDIA_ROOT =  os.path.join(BASE_DIR,"media")
    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"
else:
    MEDIA_ROOT =  '/vol/web/media'
    STATIC_URL = '/static/static/'
    MEDIA_URL = '/static/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

CRISPY_TEMPLATE_PACK = "bootstrap4"
IMPORT_EXPORT_USE_TRANSACTIONS = True
CKEDITOR_UPLOAD_PATH = "ck_uploads"


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = "ibadovfariz1999@gmail.com"
# EMAIL_HOST_PASSWORD = "swfcrfnrlzcpyyli"