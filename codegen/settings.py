# import os
# from pathlib import Path
# from dotenv import load_dotenv
# # import dj_database_url

# load_dotenv()

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'django-insecure-ru2ld7xf=%$+jt&2ku+d7sh$m2*au)!5+170al854&ii2hy7e5'
# # DEBUG = True
# DEBUG = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes")
# # ALLOWED_HOSTS = []
# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else ["127.0.0.1","localhost"]

# GEMANI_KEYS = [
#     os.getenv("GOOGLE_GEMANI_API_1"),
#     os.getenv("GOOGLE_GEMANI_API_2"),
#     os.getenv("GOOGLE_GEMANI_API_3"),
#     os.getenv("GOOGLE_GEMANI_API_4"),
# ]
# #drop
# GEMANI_KEYS = [k for k in GEMANI_KEYS if k]
# FRONTEND_URL = os.getenv("FRONTEND_URL")  # set to your Vercel URL in env vars
# if FRONTEND_URL:
#     CORS_ALLOWED_ORIGINS = [FRONTEND_URL]
# else:
#     CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]

# CORS_ALLOW_CREDENTIALS = True

# # Static files (for whitenoise)
# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_DIRS = [BASE_DIR / "static"]  # optional if you use it
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# # Session cookies (production)
# SESSION_COOKIE_SECURE = not DEBUG
# CSRF_COOKIE_SECURE = not DEBUG
# SESSION_COOKIE_SAMESITE = None  # required for cross-site cookies with credentials=True



# # -------------------------------------------
# client_id = os.getenv("GITHUB_CLIENT_ID")
# client_secret = os.getenv("GITHUB_CLIENT_SECRET")

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'corsheaders',
#     'social_django',
#     'users',
#     'convert',
# ]

# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'codegen.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'social_django.context_processors.backends',   # Added
#                 'social_django.context_processors.login_redirect',  # Added
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'codegen.wsgi.application'
# # ------------------------------------------------------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'codegen_db',
#         'USER': 'root',
#         'PASSWORD': 'Ponnadas#123',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }
# # backend/codegen/settings.py  (add after STATIC_...)



# # DATABASE_URL = os.getenv("DATABASE_URL")
# # if DATABASE_URL:
# #     DATABASES = {
# #         "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)
# #     }
# # else:
# #     # fallback to individual vars (your local dev)
# #     DATABASES = {
# #         "default": {
# #             "ENGINE": "django.db.backends.mysql",
# #             "NAME": os.getenv("DB_NAME", "codegen_db"),
# #             "USER": os.getenv("DB_USER", "root"),
# #             "PASSWORD": os.getenv("DB_PASSWORD", ""),
# #             "HOST": os.getenv("DB_HOST", "localhost"),
# #             "PORT": os.getenv("DB_PORT", "3306"),
# #         }
# #     }


# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True
# STATIC_URL = 'static/'
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH_USER_MODEL = 'users.CustomUser'
# CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True
# SESSION_COOKIE_SAMESITE = None
# SESSION_COOKIE_SECURE = False

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication'],
#     'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
# }

# # ---------------- GitHub OAuth ----------------
# SOCIAL_AUTH_GITHUB_KEY = os.getenv("GITHUB_CLIENT_ID")
# SOCIAL_AUTH_GITHUB_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.github.GithubOAuth2',  # GitHub OAuth
#     'django.contrib.auth.backends.ModelBackend',  # Default
# )

# LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/dashboard/'
# LOGOUT_REDIRECT_URL = '/'

# SOCIAL_AUTH_PIPELINE = (
#     'social_core.pipeline.social_auth.social_details',
#     'social_core.pipeline.social_auth.social_uid',
#     'social_core.pipeline.social_auth.auth_allowed',
#     'social_core.pipeline.social_auth.social_user',
#     'social_core.pipeline.user.get_username',
#     'social_core.pipeline.user.create_user',
#     'social_core.pipeline.social_auth.associate_user',
#     'social_core.pipeline.social_auth.load_extra_data',
#     'social_core.pipeline.user.user_details',
# )



# import os
# from pathlib import Path
# from dotenv import load_dotenv
# import dj_database_url

# load_dotenv()

# BASE_DIR = Path(__file__).resolve().parent.parent
# SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default")
# # DEBUG = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes")
# DEBUG = True

# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else ["127.0.0.1", "localhost"]

# # ---------- Gemini Keys ----------
# GEMANI_KEYS = [k for k in [
#     os.getenv("GOOGLE_GEMANI_API_1"),
#     os.getenv("GOOGLE_GEMANI_API_2"),
#     os.getenv("GOOGLE_GEMANI_API_3"),
#     os.getenv("GOOGLE_GEMANI_API_4"),
# ] if k]

# # ---------- CORS ----------
# FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
# CORS_ALLOWED_ORIGINS = [FRONTEND_URL]
# CORS_ALLOW_CREDENTIALS = True
# CSRF_TRUSTED_ORIGINS = [FRONTEND_URL]
# SESSION_COOKIE_SAMESITE = None
# SESSION_COOKIE_SECURE = not DEBUG
# CSRF_COOKIE_SECURE = not DEBUG

# # ---------- Static Files ----------
# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_DIRS = [BASE_DIR / "static"]
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# # ---------- Installed Apps ----------
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'corsheaders',
#     'social_django',
#     'users',
#     'convert',
# ]

# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'codegen.urls'
# WSGI_APPLICATION = 'codegen.wsgi.application'

# # ---------- Database ----------
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.mysql',
# #         'NAME': 'codegen_db',
# #         'USER': 'root',
# #         'PASSWORD': 'Ponnadas#123',
# #         'HOST': 'localhost',
# #         'PORT': '3306',
# #     }
# # }
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.getenv("DATABASE_URL", "postgresql://codegen_db_user:4NYYwPoPw1JyYIkN7SVNuvid11WfM04T@dpg-d3nhaj7diees73dna5ag-a.singapore-postgres.render.com/codegen_db")
#     )
# }
# # ---------- REST Framework ----------
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication'],
#     'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
# }

# # ---------- GitHub OAuth ----------
# SOCIAL_AUTH_GITHUB_KEY = os.getenv("GITHUB_CLIENT_ID")
# SOCIAL_AUTH_GITHUB_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.github.GithubOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )

# LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/dashboard/'
# LOGOUT_REDIRECT_URL = '/'







# import os
# from pathlib import Path
# from dotenv import load_dotenv
# import dj_database_url

# # Load environment variables
# load_dotenv()

# BASE_DIR = Path(__file__).resolve().parent.parent

# # ---------- Security ----------
# SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default")
# DEBUG = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes")

# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else ["127.0.0.1", "localhost"]

# # ---------- Gemini Keys ----------
# GEMANI_KEYS = [k for k in [
#     os.getenv("GOOGLE_GEMANI_API_1"),
#     os.getenv("GOOGLE_GEMANI_API_2"),
#     os.getenv("GOOGLE_GEMANI_API_3"),
#     os.getenv("GOOGLE_GEMANI_API_4"),
# ] if k]

# # ---------- CORS ----------
# FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
# CORS_ALLOWED_ORIGINS = [FRONTEND_URL]
# CORS_ALLOW_CREDENTIALS = True
# CSRF_TRUSTED_ORIGINS = [FRONTEND_URL]
# SESSION_COOKIE_SAMESITE = None
# SESSION_COOKIE_SECURE = not DEBUG
# CSRF_COOKIE_SECURE = not DEBUG

# # ---------- Static Files ----------
# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_DIRS = [BASE_DIR / "static"]
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# # ---------- Installed Apps ----------
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'corsheaders',
#     'social_django',
#     'users',
#     'convert',
# ]

# # ---------- Middleware ----------
# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'codegen.urls'
# WSGI_APPLICATION = 'codegen.wsgi.application'

# # ---------- Database ----------
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.getenv(
#             "DATABASE_URL",
#             "postgresql://codegen_db_user:4NYYwPoPw1JyYIkN7SVNuvid11WfM04T@dpg-d3nhaj7diees73dna5ag-a.singapore-postgres.render.com/codegen_db"
#         )
#     )
# }

# # ---------- REST Framework ----------
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication'],
#     'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
# }

# # ---------- GitHub OAuth ----------
# SOCIAL_AUTH_GITHUB_KEY = os.getenv("GITHUB_CLIENT_ID")
# SOCIAL_AUTH_GITHUB_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.github.GithubOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )

# # ---------- Redirect URLs ----------
# LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/dashboard/'
# LOGOUT_REDIRECT_URL = '/'

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------- Security ----------
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default")
DEBUG = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else ["127.0.0.1", "localhost"]
if os.environ.get("DEBUG", "True") == "True":
    ALLOWED_HOSTS += ["127.0.0.1", "localhost"]
# ---------- Custom User ----------
AUTH_USER_MODEL = 'users.CustomUser'
# Just a minimal setting so Django doesn’t complain
STATIC_URL = "/static/"


CORS_ALLOWED_ORIGINS = ["https://codegen-mocha.vercel.app"]
CSRF_TRUSTED_ORIGINS = ["https://codegen-mocha.vercel.app"]

# ---------- Gemini API Keys ----------
GEMANI_KEYS = [k for k in [
    os.getenv("GOOGLE_GEMANI_API_1"),
    os.getenv("GOOGLE_GEMANI_API_2"),
    os.getenv("GOOGLE_GEMANI_API_3"),
    os.getenv("GOOGLE_GEMANI_API_4"),
] if k]

# ---------- CORS ----------
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
CORS_ALLOWED_ORIGINS = [FRONTEND_URL]
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [FRONTEND_URL]

# ---------- Middleware ----------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------- Installed Apps ----------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # Keep this for admin CSS
    'rest_framework',
    'corsheaders',
    'social_django',
    'users',
    'convert',
]

ROOT_URLCONF = 'codegen.urls'
WSGI_APPLICATION = 'codegen.wsgi.application'

# ---------- Templates ----------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # No templates needed for API backend
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

# ---------- Database ----------
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv(
            "DATABASE_URL",
            "postgresql://codegen_db_user:4NYYwPoPw1JyYIkN7SVNuvid11WfM04T@dpg-d3nhaj7diees73dna5ag-a.singapore-postgres.render.com/codegen_db"
        )
    )
}

# ---------- REST Framework ----------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
}

# ---------- GitHub OAuth ----------
SOCIAL_AUTH_GITHUB_KEY = os.getenv("GITHUB_CLIENT_ID")
SOCIAL_AUTH_GITHUB_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# ---------- Redirect URLs ----------
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'
