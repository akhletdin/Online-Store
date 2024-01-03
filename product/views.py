'''
views.py - Файл представлений приложения.
View - это функция, которая принимает запрос и возвращает ответ.

HttpResponse - класс, который представляет собой ответ сервера.

HTTP - протокол передачи гипертекста. HyperText Transfer Protocol.
HTTPs - защищенный протокол передачи гипертекста. HyperText Transfer Protocol Secure.

Method - метод. GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD.

render - функция, которая принимает запрос, имя шаблона и словарь с данными и возвращает ответ.
принимает следующие аргументы:
request - запрос от пользователя (объект HttpRequest) параметр обязательный
template_name - имя шаблона (строка) параметр обязательный
context - словарь с данными (dict) параметр необязательный
content_type - тип контента (строка) параметр необязательный например 'text/html', 'application/json' и т.д. по умолчанию 'text/html'
status - статус ответа (число) параметр необязательный например 200, 404, 500 и т.д. по умолчанию 200 (OK)
using - имя базы данных (строка) параметр необязательный по умолчанию None (основная база данных) Нужен для работы с несколькими базами данных (подробнее в документации https://docs.djangoproject.com/en/3.2/topics/db/multi-db/)

QuerySet - набор объектов, полученных в результате запроса к базе данных.


ORM - Object-Relational Mapping - объектно-реляционное отображение.
Это технология программирования, которая связывает базы данных с концепциями объектно-ориентированных языков программирования,
создавая «виртуальную объектную базу данных». В Django ORM реализован с помощью классов моделей.

objects - менеджер модели. Менеджер модели - это интерфейс для взаимодействия с базой данных.
Менеджер позволяет обращаться к базе данных с помощью следующих методов:
.all(), .filter(), .exclude(), .get(), .create(), .update(), .delete() и т.д.
(подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/)

'''

from django.shortcuts import redirect, render
from django.http import HttpResponse
from product.models import Product, Category, Review
from product.forms import ProductCreateForm, ProductCreateForm2, CategoryCreateForm, ReviewCreateForm


def main_view(request):
    if request.method == 'GET':  # GET - получение данных
        return render(request, 'index.html')


def product_list_view(request):
    if request.method == 'GET':  # GET - получение данных
        # 1 - получить все посты из базы данных
        products = Product.objects.all()  # QuerySet

        # 2 - передать посты в шаблон
        context = {
            'products': products
        }

        return render(
            request,  # запрос от пользователя (объект HttpRequest) параметр обязательный
            'product/list.html',  # имя шаблона (строка) параметр обязательный
            context=context  # словарь с данными (dict) параметр необязательный
        )


def category_list_view(request):
    if request.method == 'GET':
        # 1 - получить все хэштеги из базы данных
        categories = Category.objects.all()

        # 2 - передать хэштеги в шаблон
        context = {
            'categories': categories,
        }

        # 3 - вернуть ответ с шаблоном и данными
        return render(
            request,  # запрос от пользователя (объект HttpRequest) параметр обязательный
            'category/categories.html.',  # имя шаблона (строка) параметр обязательный
            context=context  # словарь с данными (dict) параметр необязательный
        )


def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, '404.html')

        context = {
            'product': product,
            'form': ReviewCreateForm
        }

        return render(
            request,  # запрос от пользователя (объект HttpRequest) параметр обязательный
            'product/detail.html',  # имя шаблона (строка) параметр обязательный
            context=context  # словарь с данными (dict) параметр необязательный
        )
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST, request.FILES)

        if form.is_valid():
            # Если это Form, Product.objects.create(**form.cleaned_data)
            Review.objects.create(**form.cleaned_data)

            # Если это ModelForm, form.save()
            form.save()

            return redirect('/reviews/')

        else:
            context = {
                'form': form,
            }

        return render(request, 'product/create.html', context=context)


def product_create_view(requests):
    if requests.method == 'GET':
        context = {
            'form': ProductCreateForm2,
        }
        return render(requests, 'product/create.html', context=context)

    if requests.method == 'POST':
        form = ProductCreateForm2(requests.POST, requests.FILES)

        if form.is_valid():
            # Если это Form, Product.objects.create(**form.cleaned_data)
            # Product.objects.create(**form.cleaned_data)

            # Если это ModelForm, form.save()
            form.save()

            return redirect('/products/')

        else:
            context = {
                'form': form,
            }

        return render(requests, 'product/create.html', context=context)


def category_create_view(requests):
    if requests.method == 'GET':
        context = {
            'form': CategoryCreateForm,
        }
        return render(requests, 'category/create.html', context=context)

    if requests.method == 'POST':
        form = CategoryCreateForm(requests.POST, requests.FILES)

        if form.is_valid():
            # Если это Form, Product.objects.create(**form.cleaned_data)
            Product.objects.create(**form.cleaned_data)

            # Если это ModelForm, form.save()
            # form.save()

            return redirect('/categories/')

        else:
            context = {
                'form': form,
            }

        return render(requests, 'category/create.html', context=context)


def review_create_view(request, post_id):
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)

        try:
            product = Product.objects.get(id=post_id)
        except Product.DoesNotExist:
            return render(request, '404.html')

        if form.is_valid():
            review = form.save(commit=False)
            review.post_id = post_id
            review.save()

            return redirect(f'/products/{post_id}/')
        else:
            context = {
                'product': product,
                'form': form,
            }

            return render(request, 'product/detail.html', context=context)
