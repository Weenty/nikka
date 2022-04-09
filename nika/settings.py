from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-w3e&#cp2_15%-(84s#v7349e+q^qxp-zv_kh^1q0o*&9qh(jd)'

DEBUG = True

ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'rest_framework.authtoken',
    'ckeditor',
    "corsheaders",
    'ckeditor_uploader',
    'main',
    'goods',
    'djoser',
    'rest_framework',
    'django.contrib.staticfiles',
    'drf_yasg',
    # 'rest_framework_simplejwt',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

# SIMPLE_JWT = {
#    'AUTH_HEADER_TYPES': ('JWT',),
# }

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'findo3184@gmail.com'
EMAIL_HOST_PASSWORD = 'i33a05an'
EMAIL_PORT = 587

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'auth/users/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'auth/users/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'auth/users/activation/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,
    'SERIALIZERS': {},
    'PERMISSIONS': {
        'user_list': ['rest_framework.permissions.IsAdminUser'],
    }
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nika.urls'

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

WSGI_APPLICATION = 'nika.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

AUTH_USER_MODEL = 'main.users'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

CKEDITOR_UPLOAD_PATH = "uploads/"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
