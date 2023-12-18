"""
urls.py - Файл маршрутизации Django-проекта.

admin.site.urls - URL-адреса административного сайта.

path - функция для создания маршрута.
Принимает 2 аргумента:
1) Путь (строка)
2) Обработчик (функция, которая будет обрабатывать запрос)
"""
from django.contrib import admin
from django.urls import path
from post.views import main_view, product_list_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', product_list_view)
]