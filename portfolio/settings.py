import os
from pathlib import Path
import dj_database_url  # Import dj_database_url for parsing the database URL
from django.core.wsgi import get_wsgi_application

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-(0y2rb%-5dtgdc3h^^-u$rq05yzi2n=!j*htp$59x=j9gq*8tp'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  # ✅ यह होना चाहिए
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',  # ✅ आपका ऐप भी होना चाहिए
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'RoFWwLKsoPNuQnCktxuszqoZEDhoClNR',
        'HOST': 'turntable.proxy.rlwy.net',  # नया जेनरेट हुआ डोमेन
        'PORT': '18706',  # नया पोर्ट
        'OPTIONS': {
            'sslmode': 'require',
            'sslrootcert': 'prod-ca-2021.crt'  # SSL सर्टिफिकेट (अगर जरूरी हो)
        }
    }
}
WSGI_APPLICATION = 'portfolio.wsgi.application'



ALLOWED_HOSTS = ['*']  # अस्थायी तौर पर सभी होस्ट्स को अनुमति दें
DEBUG = False  # Production में False रखें

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

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
application = get_wsgi_application()

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'gyanbabu193@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'ulys fufa pbgw fgto'  # Use an app password, not your actual password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOGIN_URL = '/accounts/login/'

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / 'mainapp/static'
]
