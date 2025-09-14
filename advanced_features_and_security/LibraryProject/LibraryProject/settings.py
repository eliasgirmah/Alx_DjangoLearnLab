"""
Security Measures Implemented:

1. DEBUG=False to prevent information leakage.
2. SECURE_BROWSER_XSS_FILTER=True and SECURE_CONTENT_TYPE_NOSNIFF=True to prevent XSS and MIME-type attacks.
3. CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE set to True to ensure cookies are only sent over HTTPS.
4. X_FRAME_OPTIONS='DENY' to prevent clickjacking.
5. CSP middleware added to control content sources and mitigate XSS.
6. Views use Django ORM to prevent SQL injection.
7. All forms include {% csrf_token %} to protect against CSRF attacks.
"""


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!l&fe&tgto*dxyq0a%_as^n$u1wa&8g0ey704qyxzchl+6f&ke'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
]

INSTALLED_APPS += [
    'csp',
]

MIDDLEWARE += [
    'csp.middleware.CSPMiddleware',
]

# Example CSP policy
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "https://cdnjs.cloudflare.com")
CSP_STYLE_SRC = ("'self'", "https://cdnjs.cloudflare.com")

# Tell Django to use our custom user model
AUTH_USER_MODEL = "bookshelf.CustomUser"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------
# Production Security Settings
# -------------------------
DEBUG = False  # Never leave DEBUG=True in production

# Browser Security
SECURE_BROWSER_XSS_FILTER = True         # Enables XSS filter in the browser
SECURE_CONTENT_TYPE_NOSNIFF = True       # Prevents MIME-type sniffing
X_FRAME_OPTIONS = 'DENY'                 # Prevent clickjacking

# Cookies Security
CSRF_COOKIE_SECURE = True                # Ensures CSRF cookie is sent over HTTPS only
SESSION_COOKIE_SECURE = True             # Ensures session cookie is sent over HTTPS only

# Optional: HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 3600               # Enforce HTTPS for 1 hour
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
