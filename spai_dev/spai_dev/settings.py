"""
Django settings for spai_dev project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5qhlplha*3#*!4lv$)$de2_($ky+lo^^q-!l8%qb1wqk61d=!i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.5', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'spai_app',
    'rest_framework'
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

ROOT_URLCONF = 'spai_dev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'spai_app.context_processors.get_image_of_user'
            ],
        },
    },
]

WSGI_APPLICATION = 'spai_dev.wsgi.application'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # MySQL backend
        'NAME': 'spai_check',  # Database name
        'USER': 'root',  # Database user
        'PASSWORD': 'root',  # Database password
        'HOST': 'localhost',  # Database host, use 'localhost' or the IP of your MySQL server
        'PORT': '3306',  # MySQL default port
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'spai123',
#         'HOST':'localhost',
#         'PORT':'5432',
#         'USER':'postgres',
#         'PASSWORD':'windows'
#     }
# }
import mimetypes

mimetypes.add_type("text/css", ".css", True)
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "spai_app.User"

USER_CREATED = "user_created"
USER_DETAILS_ADDED = "user_details_added"
ADMIN_APPROVAL_PENDING = "admin_approval_pending"
ADMIN_APPROVED = "admin_approved"
ADMIN_REJECTED = "admin_rejected"
PAYMENT_PENDING = "payment_pending"
PAYMENT_DONE = "payment_completed"
EX_1_APPROVAL_PENDING = "executive_1_approval_pending"
EX_2_APPROVAL_PENDING = "executive_2_approval_pending"
EX_1_APPROVED = "executive_1_approved"
EX_2_APPROVED = "executive_2_approved"
EMAIL_SEND = "email_send_to_the_user"
PASSWORD_RESET = "password_changed"

QR_CODE = 1
BANK_TRANSFER = 2
PAYMENT_TYPE = ((QR_CODE, "QR CODE"), (BANK_TRANSFER, "BANK TRANSFER"))
QR_CODE_NAME = "QR code"
BANK_TRANSFER_NAME = "Bank Transfer"

ADMIN_ROLE_VALUE = 1
MEMBER_ROLE_VALUE = 2
ROLE_CHOICES = ((ADMIN_ROLE_VALUE, "ADMIN"), (MEMBER_ROLE_VALUE, "MEMBER"))

SECRETARY = 1
PRESIDENT = 2
EXECUTIVE_CHOICES = ((SECRETARY, "SECRETARY"), (PRESIDENT, "PRESIDENT"))



STATE_CHOICES = [
    ("", "Select state"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal")
]


# login session info
SESSION_COOKIE_AGE = 43200


# smtp email service
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'spai05138@gmail.com'
EMAIL_HOST_PASSWORD = 'cbycsxyyvldqrsrg'

# """
# Django settings for spai_dev project.
#
# Generated by 'django-admin startproject' using Django 5.0.6.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/5.0/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/5.0/ref/settings/
# """
#
# import os
# from pathlib import Path
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-5qhlplha*3#*!4lv$)$de2_($ky+lo^^q-!l8%qb1wqk61d=!i'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = ['spaionline.pythonanywhere.com']
#
# # Application definition
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'spai_app',
#     'rest_framework'
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'spai_dev.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'spai_dev.wsgi.application'
#
# # Database
# # https://docs.djangoproject.com/en/5.0/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'spaionline$default',
#         'USER': 'spaionline',
#         'PASSWORD': 'spaiadmin',
#         'HOST': 'spaionline.mysql.pythonanywhere-services.com',
#         'PORT': '3306',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         }
#     }
# }
#
# import mimetypes
#
# mimetypes.add_type("text/css", ".css", True)
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
#
# STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
#
# # Password validation
# # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
# # Internationalization
# # https://docs.djangoproject.com/en/5.0/topics/i18n/
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'Asia/Kolkata'

# USE_L10N = True
#
# USE_I18N = True
#
# USE_TZ = True
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.0/howto/static-files/
#
# STATIC_URL = 'static/'
#
# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# AUTH_USER_MODEL = "spai_app.User"
#
# USER_CREATED = "user_created"
# USER_DETAILS_ADDED = "user_details_added"
# ADMIN_APPROVAL_PENDING = "admin_approval_pending"
# ADMIN_APPROVED = "admin_approved"
# ADMIN_REJECTED = "admin_rejected"
# PAYMENT_PENDING = "payment_pending"
# PAYMENT_DONE = "payment_completed"
# EMAIL_SEND = "email_send_to_the_user"
# PASSWORD_RESET = "password_changed"
#
# QR_CODE = 1
# BANK_TRANSFER = 2
# PAYMENT_TYPE = ((QR_CODE, "QR CODE"), (BANK_TRANSFER, "BANK TRANSFER"))
# QR_CODE_NAME = "QR code"
# BANK_TRANSFER_NAME = "Bank Transfer"
#
# ADMIN_ROLE_VALUE = 1
# MEMBER_ROLE_VALUE = 2
# ROLE_CHOICES = ((ADMIN_ROLE_VALUE, "ADMIN"), (MEMBER_ROLE_VALUE, "MEMBER"))
#
# STATE_CHOICES = [
#     ("", "Select state"),
#     ("Andhra Pradesh", "Andhra Pradesh"),
#     ("Arunachal Pradesh", "Arunachal Pradesh"),
#     ("Assam", "Assam"),
#     ("Bihar", "Bihar"),
#     ("Chhattisgarh", "Chhattisgarh"),
#     ("Goa", "Goa"),
#     ("Gujarat", "Gujarat"),
#     ("Haryana", "Haryana"),
#     ("Himachal Pradesh", "Himachal Pradesh"),
#     ("Jharkhand", "Jharkhand"),
#     ("Karnataka", "Karnataka"),
#     ("Kerala", "Kerala"),
#     ("Madhya Pradesh", "Madhya Pradesh"),
#     ("Maharashtra", "Maharashtra"),
#     ("Manipur", "Manipur"),
#     ("Meghalaya", "Meghalaya"),
#     ("Mizoram", "Mizoram"),
#     ("Nagaland", "Nagaland"),
#     ("Odisha", "Odisha"),
#     ("Punjab", "Punjab"),
#     ("Rajasthan", "Rajasthan"),
#     ("Sikkim", "Sikkim"),
#     ("Tamil Nadu", "Tamil Nadu"),
#     ("Telangana", "Telangana"),
#     ("Tripura", "Tripura"),
#     ("Uttar Pradesh", "Uttar Pradesh"),
#     ("Uttarakhand", "Uttarakhand"),
#     ("West Bengal", "West Bengal")
# ]
#
# # login session info
# SESSION_COOKIE_AGE = 43200
#
# # smtp email service
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'spai05138@gmail.com'
# EMAIL_HOST_PASSWORD = 'cbycsxyyvldqrsrg'
# MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
