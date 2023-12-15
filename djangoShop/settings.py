"""
settings.py - Файл настроек Django-проекта.
"""

from pathlib import Path

# Корневая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent


# Секретный ключ проекта (используется для шифрования данных)
SECRET_KEY = 'django-insecure-0c0j9-gkxsv-z=g#viu_34ka8vz9xxiux+x9_o386qkn!j)#!^'

# Режим отладки (включен/выключен)
DEBUG = True

# Список разрешенных хостов для проекта
ALLOWED_HOSTS = ['*']

# Список приложений, установленных в проекте
INSTALLED_APPS = [
    # Internal apps
    'django.contrib.admin', # Административный сайт
    'django.contrib.auth', # Аутентификация пользователей (авторизация)
    'django.contrib.contenttypes', # Работа с контентом (содержимым)
    'django.contrib.sessions', # Работа с сессиями
    'django.contrib.messages', # Работа с сообщениями (вывод сообщений пользователю)
    'django.contrib.staticfiles', # Работа со статическими файлами (css, js, img)

    # External apps

    # My apps
    'post', # Приложение для работы с постами
]

# Список промежуточных слоев (middleware) для проекта
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Работа с безопасностью
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF - корневой URL-адрес проекта
ROOT_URLCONF = 'djangoShop.urls'

# Темплейтинг (шаблонизация) - работа с шаблонами
# (файлами html, которые будут отображаться в браузере)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates", # Папка, в которой будут храниться шаблоны
        ], # Папки, в которых будут храниться шаблоны
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

# WSGI_APPLICATION - файл, который будет запускаться при запуске проекта
WSGI_APPLICATION = 'djangoShop.wsgi.application'


# DATABASES - настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Тип базы данных
        'NAME': BASE_DIR / 'db.sqlite3', # Путь к файлу базы данных
    }
}


# AUTH_PASSWORD_VALIDATORS - настройки валидации паролей пользователей
# UserAttributeSimilarityValidator - проверка на схожесть с именем пользователя
# MinimumLengthValidator - проверка на минимальную длину пароля
# CommonPasswordValidator - проверка на распространенность пароля
# NumericPasswordValidator - проверка на наличие цифр в пароле
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


# LANGUAGE_CODE - язык проекта
LANGUAGE_CODE = 'en-us'

# TIME_ZONE - часовой пояс проекта
TIME_ZONE = 'Asia/Bishkek' # Asia/Bishkek +6

# USE_I18N - использование мультиязычности
USE_I18N = True

# USE_TZ - использование часовых поясов
USE_TZ = True


# STATIC_URL - URL-адрес статических файлов (css, js, img)
STATIC_URL = 'static/'

# DEFAULT_AUTO_FIELD - тип поля для первичного ключа
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'