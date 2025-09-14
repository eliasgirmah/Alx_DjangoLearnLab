"""
Security Measures Implemented:

1. DEBUG=False to prevent information leakage in production.
2. SECURE_BROWSER_XSS_FILTER=True and SECURE_CONTENT_TYPE_NOSNIFF=True 
   to protect against XSS and MIME-type attacks.
3. CSRF_COOKIE_SECURE=True and SESSION_COOKIE_SECURE=True 
   to ensure cookies are transmitted only over HTTPS.
4. X_FRAME_OPTIONS='DENY' to prevent clickjacking attacks.
5. CSP middleware is added (django-csp) to control content sources and mitigate XSS risks.
6. Views use Django ORM to prevent SQL injection by safely handling user input.
7. All forms include {% csrf_token %} in templates to protect against CSRF attacks.
8. SECURE_SSL_REDIRECT=True forces all HTTP traffic to HTTPS.
9. SECURE_HSTS_SECONDS, SECURE_HSTS_INCLUDE_SUBDOMAINS, and SECURE_HSTS_PRELOAD 
   enforce HSTS to ensure browsers access the site only via HTTPS.
"""

from pathlib import Path

# -------------------------
# Base Directory
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# Security & Deployment
# -------------------------
SECRET_KEY = 'django-insecure-!l&fe&tgto*dxyq0a%_as^n$u1wa&8g0ey704qyxzchl+6f&ke'
DEBUG = False  # Never leave DEBUG=True in production
ALLOWED_HOSTS = ['yourdomain.com']  # Replace with your production domain

# -------------------------
# Installed Apps
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bookshelf',
    'relationship_app',

    'csp',  # Content Security Policy
]

# -------------------------
# Middleware
# -------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'csp.middleware.CSPMiddleware',  # CSP Middleware
]

# -------------------------
# URL & Templates
# -------------------------
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

# -------------------------
# Database
# -------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------
# Password Validation
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------
# Internationalization
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------
# Static Files
# -------------------------
STATIC_URL = 'static/'

# -------------------------
# Default Primary Key Field
# -------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------
# Custom User Model
# -------------------------
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# -------------------------
# HTTPS / SSL / Security
# -------------------------
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# -------------------------
# Content Security Policy (CSP)
# -------------------------
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "https://cdnjs.cloudflare.com")
CSP_STYLE_SRC = ("'self'", "https://cdnjs.cloudflare.com")
