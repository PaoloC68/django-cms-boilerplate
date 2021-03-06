# -*- coding: utf-8 -*-
import os
import dj_database_url

gettext = lambda s: s

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Admin', '<admin-email>')
)

MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config(default='postgres://postgres:@localhost:5432/brcms')}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'additional_static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0r6%7gip5tmez*vygfv+u14h@4lbt^8e2^26o#5_f_#b7%cm)u'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

CMS_TEMPLATES = (
    ('sample.html', 'Sample Template'),
    ('ventus/simple.html', 'Ventus Simple'),
    ('ventus/standard.html', 'Ventus Standard Page'),
    ('ventus/homepage.html', 'Ventus HomePage'),
)
# i18n and l10n
CMS_HIDE_UNTRANSLATED = True
LANGUAGES = (
    ('pt', gettext("Portugues")),
    ('en', gettext("English")),
    ('it', gettext("Italiano")),
)


CMS_LANGUAGES = {
    1: [
        {
            'code': 'pt',
            'name': gettext('Portugues'),
            'fallbacks': ['it', 'en'],
            'public': True,
            'hide_untranslated': False,
            'redirect_on_fallback':True,
        },
        {
            'code': 'en',
            'name': gettext('English'),
            'fallbacks': ['de', 'fr'],
            'public': True,
            'hide_untranslated': False,
            'redirect_on_fallback':True,
        },

        {
            'code': 'it',
            'name': gettext('Italiano'),
            'public': True,
            'hide_untranslated': False,
            'redirect_on_fallback':True,
        },
    ],


    'default': {
        'fallbacks': ['pt', 'en'],
        'redirect_on_fallback':True,
        'public': False,
        'hide_untranslated': False,
    }
}

LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_CODE = 'it'
LOCALE = 'it'
MODELTRANSLATION_DEFAULT_LANGUAGE = 'it'
URLI18N_INCLUDE_PATHS = ['/', '/admin', '^/admin[-\w/]+/$']
URLI18N_ALWAYS_SHOW_LANGUAGE = True
DEFAULT_LANGUAGE = 2

CMS_PLACEHOLDER_CONF = {
    'new-image': {
        'plugins': ['PicturePlugin'],
        'name':gettext("Picture"),
    },
    'new-text': {
        'plugins': ['TextPlugin'],
        'name':gettext("Text and Link"),
    },
    'new-text-and-link': {
        'plugins': ['TextPlugin', 'LinkPlugin'],
        'name':gettext("New #2 Text"),
    },
}

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'cms',
    'menus',
    'mptt',
    'south',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'cmsplugin_contact',
    'sekizai',
    'django_extensions',
)



try:
    from local_settings import *
except ImportError:
    pass

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },

        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
            }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
