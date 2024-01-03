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
    'jazzmin',

    # Internal apps
    'django.contrib.admin',  # Административный сайт
    'django.contrib.auth',  # Аутентификация пользователей (авторизация)
    'django.contrib.contenttypes',  # Работа с контентом (содержимым)
    'django.contrib.sessions',  # Работа с сессиями
    'django.contrib.messages',  # Работа с сообщениями (вывод сообщений пользователю)
    'django.contrib.staticfiles',  # Работа со статическими файлами (css, js, img)

    # External apps

    # My apps
    'product',  # Приложение для работы с продуктами
    'user',  # Приложение для работы с пользователями
]

# Список промежуточных слоев (middleware) для проекта
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Работа с безопасностью
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
            BASE_DIR / "templates",  # Папка, в которой будут храниться шаблоны
        ],  # Папки, в которых будут храниться шаблоны
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
        'ENGINE': 'django.db.backends.sqlite3',  # Тип базы данных
        'NAME': BASE_DIR / 'db.sqlite3',  # Путь к файлу базы данных
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
LANGUAGE_CODE = 'ru-ru'

# TIME_ZONE - часовой пояс проекта
TIME_ZONE = 'Asia/Bishkek'  # Asia/Bishkek +6

# USE_I18N - использование мультиязычности
USE_I18N = True

# USE_TZ - использование часовых поясов
USE_TZ = True

# STATIC_URL - URL-адрес статических файлов (css, js, img)
STATIC_URL = 'static/'  # Как достать файл в браузере
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Расположение папки
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# DEFAULT_AUTO_FIELD - тип поля для первичного ключа
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "35-1",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "35-1 shop",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "35-1",

    # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": "books/img/logo.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the library",

    # Copyright on the footer
    "copyright": "Acme Library Ltd",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # Is you want to use a single search field you don't need to use a list, you can use a simple string
    "search_model": ["auth.User", "auth.Group"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": "navbar-success",
    "accent": "accent-indigo",
    "navbar": "navbar-lightblue navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": True,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-maroon",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "sketchy",
    "dark_mode_theme": "cyborg",
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}