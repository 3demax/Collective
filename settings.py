"""
Django settings for drwc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's=z2!dm0wiRthbdcob4)0imf5-rnjw(ovz%cqsvtg84#x_x!_'

#==============================================================================
# Debug/producation
#==============================================================================

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
try:
    DEBUG = os.environ['DEBUG'] == 'True'
    TEMPLATE_DEBUG = DEBUG
except KeyError:
    DEBUG = False
    TEMPLATE_DEBUG = False

DEBUG = True

#==============================================================================
# Stuff
#==============================================================================
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'south',
    'post',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

#==============================================================================
# Databases
#==============================================================================
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

DATE_INPUT_FORMATS = (
    '%d.%m.%Y',
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
)

#==============================================================================
# Localization
#==============================================================================
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
TIME_ZONE = 'Europe/Kiev'
LANGUAGE_CODE = 'en-us'
DATE_FORMAT = 'd E Y'
# TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True

#==============================================================================
# Tweaks
#==============================================================================
#automatically append slash to addresses
APPEND_SLASH = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

#dirty, dirty hack
# LOGIN_REDIRECT_URL = "/"

#==============================================================================
# Storages
#==============================================================================

LOGIN_URL="/login/"
LOGIN_REDIRECT_URL='/'

#==============================================================================
# Storages
#==============================================================================
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"), #'/var/www/static/',
)

# uploaded media
MEDIA_ROOT = (os.path.join(BASE_DIR, "media"))
MEDIA_URL = "/media/"

#==============================================================================
# django-crispy-forms
#==============================================================================
CRISPY_TEMPLATE_PACK = 'bootstrap'