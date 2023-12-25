'''
admin.py - Файл настроек административного сайта.

admin - модуль для работы с административным сайтом.
site - объект, который представляет собой административный сайт.
register - метод, который регистрирует модель в административном сайте. (простая регистрация)
'''

from django.contrib import admin  # модуль для работы с административным сайтом.
from django.http.request import HttpRequest # модуль для работы с административным сайтом.


from product.models import Product, Category


# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'grade', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    # readonly_fields = ['title', 'grade']
    search_fields = ['title', 'text']
    list_filter = ['grade', 'created_at']
    ordering = ['created_at']

    # def has_add_permission(self, request: HttpRequest) -> bool:
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Category)


