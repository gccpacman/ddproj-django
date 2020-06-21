"""
Django settings for ddproj project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/ent/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u73)$u^l*_qx)^^^-_m*kl(s+z$w^8riu7d)8uba%-r@2_ygx='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', 
    'django.contrib.auth',
    'django.contrib.contenttypes', 
    'django.contrib.sessions',
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'corsheaders',
    'rest_framework', 
    # 'django_filters', 
    'ddsrc'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'ddproj.urls'

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS':
#     'rest_framework.pagination.PageNumberPagination',
#     'DEFAULT_FILTER_BACKENDS':
#     ['django_filters.rest_framework.DjangoFilterBackend'],
#     'PAGE_SIZE':
#     10
# }

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

WSGI_APPLICATION = 'ddproj.wsgi.application'

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ddproj',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'connect_timeout': 5
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

ACCESS_KEY_ID = "LTAI4FwMLrrkSEskd3D5kZdx"
ACCESS_KEY_SECRET = "XAts7YVvvTNsyqMYa0gE6YLDH4q13B"

# The URL of AliCloud OSS endpoint
# Refer https://www.alibabacloud.com/help/zh/doc-detail/31837.htm for OSS Region & Endpoint
# END_POINT = "oss-cn-shanghai.aliyuncs.com"
# BUCKET_NAME = "datadudexyz"  # if not exist in aliyun oss platform, it will created automatically
# ALIYUN_OSS_CNAME = ""  # custom domain. optional
# BUCKET_ACL_TYPE = "private"  # bucket access type. available value: private, public-read, public-read-write
# ALIYUN_OSS_HTTPS = True  # optional config. determine use https or not. if not declare, this value will be False by default.

# Qiniu
QINIU_ACCESS_KEY = "YQxexGbLS7jFWHcWG-11rtNlap7b3tkBjrzY2YyU"
QINIU_SECRET_KEY = "N2oppcLV1lOXnZNhJ2FXAzFcO3mzTA3UcOw1Qvi8"
QINIU_BUCKET_NAME = "ddxyzstatic"
QINIU_BUCKET_DOMAIN = "static.datadude.xyz"
QINIU_SECURE_URL = False

# storage media file
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'
MEDIA_ROOT = '/_dev/media/'

# storage static file
STATICFILES_STORAGE = 'qiniustorage.backends.QiniuStaticStorage'
STATIC_ROOT = '/_dev/static/'
STATIC_URL = 'http://static.datadude.xyz/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "ddfront/dist/static"),
# ]

SHANGHAI_LIBRARY_API_KEY = '3f5df65840c93fea3c1026b8a64649dffa3d6328'
BAIDU_MAP_JSAPI_KEY = 'bRrHftKV7wBPHYFSkp2GRZQCVGbz8nhy'
GAODE_MAP_WEBAPI_KEY = '82455bd226d65b5c36768ad1cd410fea'

# local memory cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:8080',
]

if os.environ.get('DD_BACKEND_ENV') == 'PROD':
    DEBUG = False
    CORS_ORIGIN_REGEX_WHITELIST = [
        r"^\w+://\w+\.datadude\.xyz$",
    ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'ddproj',
            'USER': 'root',
            'PASSWORD': 'tcs@SIN2',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
                'connect_timeout': 5
            },
        }
    }
elif os.environ.get('DD_BACKEND_ENV') == 'DEV':
    DEBUG = False

