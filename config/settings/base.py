"""
Settings for sync-web

Django settings documentation
https://docs.djangoproject.com/en/dev/topics/settings/

Django settings reference
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import environ
env = environ.Env()

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('app')


# WEBSITE
# ------------------------------------------------------------------------------

WEBSITE_NAME = 'sync-web'


# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.steam',
    'allauth.socialaccount.providers.twitch',

    'bootstrap4',
    'compressor',
    'sass_processor',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'app.accounts.apps.AccountsConfig',
    'app.common',
    'app.pages.apps.PagesConfig',
    'app.users.apps.UsersConfig',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'app.contrib.sites.migrations'
}


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', False)


# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)


# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
ADMINS = (
    ("""admin""", 'demine0@gmail.com'),
)

MANAGERS = ADMINS


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------

STATIC_ROOT = str(ROOT_DIR('staticfiles'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    'sass_processor.finders.CssFinder',
)


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

MEDIA_ROOT = str(APPS_DIR('media'))
MEDIA_URL = '/media/'


# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

ADMIN_URL = r'^admin/'


# PASSWORD STORAGE SETTINGS
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]


# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = 'pages:homepage'
LOGIN_URL = 'account_login'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USER_DISPLAY = 'app.accounts.models.user_display_name'

ACCOUNT_FORMS = {
    'signup': 'app.accounts.forms.EmailUserSignupForm',
    'reset_password': 'app.accounts.forms.ResetPasswordForm',
}

# Email verification
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7

ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False

# Social account
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = False
SOCIALACCOUNT_ADAPTER = 'app.accounts.adapter.SocialAccountAdapter'

SOCIALACCOUNT_FORMS = {
    'signup': 'app.accounts.forms.SocialUserSignupForm',
}

# BOOTSTRAP4
# ------------------------------------------------------------------------------

BOOTSTRAP4 = {
    'set_placeholder': False,
}