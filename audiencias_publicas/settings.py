"""
Django settings for audiencias_publicas project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from decouple import config, Csv
from dj_database_url import parse as db_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY', default='secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'apps.core',
    'apps.accounts',
    'apps.notification',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'constance',
    'constance.backends.database',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'crispy_forms',
    'corsheaders',
    'debug_toolbar',
    'macros',

    'mozilla_django_oidc',

    'djangobower',
    'compressor',
    'compressor_toolkit',
    'channels',
    'channels_presence',
    'django_js_reverse',
)

AUTH_USER_MODEL = 'accounts.User'

SITE_ID = 1

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'GET',
    'OPTIONS',
    'POST',
)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'apps.core.permissions.ApiKeyPermission',
    # ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

CAMARA_LOGIN = config('CAMARA_LOGIN', default=False, cast=bool)
QUESTION_MIN_UPVOTES = config('QUESTION_MIN_UPVOTES', default=3, cast=int)
GOOGLE_ANALYTICS_ID = config('GOOGLE_ANALYTICS_ID', default='')
OLARK_ID = config('OLARK_ID', default='')
WEBSERVICE_URL = config('WEBSERVICE_URL', default='')
RECAPTCHA_SITE_KEY = config('RECAPTCHA_SITE_KEY', default='')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY', default='')

MIDDLEWARE = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mozilla_django_oidc.middleware.SessionRefresh',
    'corsheaders.middleware.CorsMiddleware',
    'apps.accounts.middlewares.AudienciasRemoteUser',
)

# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     #'corsheaders.middleware.CorsMiddleware',
#     'mozilla_django_oidc.middleware.SessionRefresh',
# )

ROOT_URLCONF = 'audiencias_publicas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'constance.context_processors.config',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'audiencias_publicas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME', default='audiencias'),
        'USER': config('DATABASE_USER', default='root'),
        'PASSWORD': config('DATABASE_PASSWORD', default='audiencias'),
        'HOST': config('DATABASE_HOST', default='localhost'),
        'PORT': config('DATABASE_PORT', default=''),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGES = (
    ('en', 'English'),
    ('pt-br', 'Brazilian Portuguese'),
)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = config('STATIC_URL', default='/static/')

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'public'))

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'templates/components/edem-navigation/static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
]

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'static')

BOWER_INSTALLED_APPS = [
    'jquery#~2.2.0',
    'foundation-sites#~6.2.4',
    'mixitup#~2.1.11',
    'https://github.com/labhackercd/fontastic-labhacker.git',
    'https://github.com/joewalnes/reconnecting-websocket.git',
    'jquery-ui#~1.12.1',
]

BOWER_PATH = os.path.join(BASE_DIR, 'node_modules/.bin/bower')
BROWSERIFY = os.path.join(BASE_DIR, 'node_modules/.bin/browserify')

COMPRESS_NODE_MODULES = os.path.join(BASE_DIR, 'node_modules')
COMPRESS_NODE_SASS_BIN = os.path.join(BASE_DIR, 'node_modules/.bin/node-sass')
COMPRESS_POSTCSS_BIN = os.path.join(BASE_DIR, 'node_modules/.bin/postcss')

COMPRESS_PRECOMPILERS = [
    ('text/x-scss', 'compressor_toolkit.precompilers.SCSSCompiler'),
    ('text/es6', BROWSERIFY + ' {infile} -t babelify --outfile {outfile}')
]

COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_OFFLINE = config('COMPRESS_OFFLINE', default=False)

LIBSASS_SOURCEMAPS = 'DEBUG'

if DEBUG:
    COMPRESS_SCSS_COMPILER_CMD = '{node_sass_bin}' \
                                 ' --source-map true' \
                                 ' --source-map-embed true' \
                                 ' --source-map-contents true' \
                                 ' --output-style expanded' \
                                 ' {paths} "{infile}" "{outfile}"' \
                                 ' &&' \
                                 ' {postcss_bin}' \
                                 ' --use "{node_modules}/autoprefixer"' \
                                 ' --autoprefixer.browsers' \
                                 ' "{autoprefixer_browsers}"' \
                                 ' -r "{outfile}"'

# Authentication stuffs
URL_PREFIX = config('URL_PREFIX', default='')
OIDC_RP_CLIENT_ID = '0949df8a7aaa7fc0a0ddcc290b5a6b9227bc1993536f6afadb7676a740115765' #Local
OIDC_RP_CLIENT_SECRET = '8f2e3a51e74c484aa8a5526d2a0b780d593f5f990ad38a33a708105fa1e6c2f4' #Local
OIDC_OP_AUTHORIZATION_ENDPOINT = 'http://localhost:3000/oauth/authorize' #Local
OIDC_OP_TOKEN_ENDPOINT = 'http://localhost:3000/oauth/token' #Local
OIDC_OP_USER_ENDPOINT = 'http://localhost:3000/oauth/userinfo' #Local
OIDC_RP_SIGN_ALGO = 'RS256' #Local
OIDC_OP_JWKS_ENDPOINT = 'http://localhost:3000/oauth/discovery/keys' #Local
LOGIN_REDIRECT_URL = '/' #Local
LOGOUT_REDIRECT_URL = '/' #Local
OIDC_RP_SCOPES = 'openid profile email' #Local
OIDC_VERIFY_JWT = False #Local
OIDC_USE_NONCE = False #Local

SESSION_COOKIE_NAME = config('SESSION_COOKIE_NAME', default='sessionid')
SESSION_COOKIE_PATH = config('SESSION_COOKIE_PATH', default='/')

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'},
    'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,
}

# Social auth
if config('ENABLE_REMOTE_USER', default=0, cast=bool):
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'apps.core.login.MyOIDCAB',
    )
else:
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'apps.core.login.MyOIDCAB',
    )

# Email configuration

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=6379)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='admin@admin.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='admin')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='')

CHANNEL_LAYERS = {
    "default": {
        # This example app uses the Redis channel layer implementation asgi_redis
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "capacity": "5000",
            "hosts": [(config('REDIS_SERVER', default='localhost'), 6379)],
        },
        "ROUTING": "apps.core.routing.channel_routing",
    },
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO'
        },
        'chat': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'mozilla_django_oidc': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    },
}

NOTIFICATION_EMAIL_LIST = config(
    'NOTIFICATION_EMAIL_LIST',
    cast=Csv(lambda x: x.strip().strip(',').strip()),
    default=''
)

# EDITABLE SETTINGS
CONSTANCE_CONFIG = {
    'SITE_NAME': ('Senado', 'Nome do site', str),
    'HOME_DESCRIPTION': ('Acompanhe ao vivo e participe enviando perguntas aos '
                         'senadores!', 'Descricao que acompanha a logo', str),
    'QUESTIONS_DESCRIPTION': ('Faca sua pergunta ou apoie outra ja feita. As '
                              'perguntas mais votadas serao encaminhadas a '
                              'Mesa para serem respondidas.', 'Descricao da '
                              'aba de perguntas', str),
    'ROOM_OBJECT': ('Pauta', 'Titulo do objeto da reuniao', str),
    'WORDS_BLACK_LIST': (
        'merda, cu, cuzao, cuzona, cusao, cusona, bunda, fodido, fodida, foda, foder, '
        'fodedor, fudido, fudida, fuder, chupa, chupada, chupador, chupadora, '
        'boquete, boqueteira, boquetera, boketeira, boketera, xupa, xupada, xupador, '
        'xupadora, pauduro, pauzudo, xoxota, chochota, buceta, boceta, busseta, '
        'bosseta, cacete, cassete, caceta, kacete, kassete, caralho, karalho, '
        'caraleo, pinto, pica, rola, roludo, gozado, gozada, goso, gosa, gosado, '
        'gosado, puta, puto, putinho, putinha, putona, putana, putaria, grelo, '
        'grelinho, filhodaputa, filhosdaputa, puta, fdps, siririca, punheta, trepar, '
        'trepada, trepadeira, caralho, caralhu, karalho, karalhu, tomarnocu, '
        'tomanocu, vadia, bosta, quenga, rabo, bolsa, cuzinho, piroca, pqp, puta que '
        'pariu, porra, carai, cu, viado, fdp, vtnc, corno, bicha, bixa, viado, viadinho, '
        'pederasta, filho da puta, bundao, bundao, filho de uma egua, '
        'filho de uma egua, achacador, achacadora, achacadores, achacar, babaca, '
        'bucetas, cagar, cagaram, cambada, caraleo, corja, cornao, covarde, covardes, '
        'cretino, cus, cus, cusao, cuzao, cuzinho, cuzona, danar, desgraca, drosoba, '
        'enrabar, escoria, escroto, escrotas, escrotos, fodao, fodona, fudendo, '
        'fuder, idiota, imundo, imundos, ku, ku, lascar, merdas, patifaria, pilantra, '
        'pilantragem, pilantras, poha, porcaria, putas, putos, sacanagem, safadeza, '
        'safado, safados, salafrario, salafrarios, vagabundagem, vagabundo, '
        'vagabundos, veadinho, veadinhos',
        'Lista de palavras e termos censurados. Devem ser separadas por '
        'virgula.',
        str
    )
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Geral': ('SITE_NAME', 'WORDS_BLACK_LIST'),
    'Pagina inicial': ('HOME_DESCRIPTION', ),
    'Pagina de sala': ('QUESTIONS_DESCRIPTION', 'ROOM_OBJECT'),
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
