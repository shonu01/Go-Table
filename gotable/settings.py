import os
from pathlib import Path

# ✅ Define BASE_DIR properly
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-4y60l*+7oylx4-9m8ru(km^g4p3n#5sv2#q1hmtwk7)z%pw^qs'

DEBUG = True

# ✅ Set allowed hosts correctly
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]  # Change this for production

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurant',  # ✅ Ensure your app is correctly listed
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

ROOT_URLCONF = 'gotable.urls'

# ✅ Fix Template Loading Issue
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "restaurant" / "templates"],  # ✅ Correct path
        'APP_DIRS': True,  # ✅ Also loads app-level templates automatically
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

WSGI_APPLICATION = 'gotable.wsgi.application'

# ✅ Database Configuration (Ensure SQLite is used correctly)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ Password Validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Language & Timezone
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Static & Media Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "restaurant" / "static"]  # ✅ Ensure this folder exists
STATIC_ROOT = BASE_DIR / "staticfiles"  # Used for collectstatic

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"  # ✅ Ensure this folder exists

# ✅ Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
