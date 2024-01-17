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

Field lookups - поиск по полям. Поиск по полям позволяет получить объекты, у которых значение поля удовлетворяет условию.
__icontains - нечувствительный к регистру поиск подстроки в строке (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#icontains)
__contains - чувствительный к регистру поиск подстроки в строке (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#contains)\
__in - поиск в списке (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#in)
__gt - больше (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#gt)
__gte - больше или равно (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#gte)
__lt - меньше (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#lt)
__lte - меньше или равно (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#lte)
__range - в диапазоне (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#range)
__year - год (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#year)
__month - месяц (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#month)
__day - день (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#day)
__week_day - день недели (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#week-day)
__hour - час (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#hour)
__minute - минута (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#minute)
__second - секунда (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#second)
__isnull - проверка на None (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#isnull)
__exact - точное совпадение (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#exact)
__iexact - нечувствительный к регистру поиск точного совпадения (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#iexact)
__startswith - начинается с (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#startswith)
__istartswith - нечувствительный к регистру поиск начинается с (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#istartswith)
__endswith - заканчивается на (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#endswith)
__iendswith - нечувствительный к регистру поиск заканчивается на (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#iendswith)
__regex - регулярное выражение (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#regex)
__iregex - нечувствительный к регистру поиск регулярного выражения (подробнее в документации https://docs.djangoproject.com/en/3.2/ref/models/querysets/#iregex)
Можно использовать с помощью методов:
.filter(), .exclude(), .get(), .create(), .update(), .delete() и т.д.
Например:
Post.objects.filter(title__icontains='привет', author__username='admin')
Можно комбинировать несколько поисковых фильтров, например:
Post.objects.filter(title__icontains='привет', author__username='admin')
Также через 2 подчеркивания можно обращаться к полям связанных моделей, например:
Post.objects.filter(author__username='admin')
Post.objects.filter(author__username__icontains='admin')
Таким образом мы можем получить все посты, у которых автор имеет имя admin.
pagination - пагинация. Пагинация - это разбиение большого количества данных на страницы.

Pagination formula:
start = (page - 1) * limit
end = page * limit
[|0, 1, 2,| 3, 4, 5,| 6, 7, 8,| 9] - список объектов
10 / 3 = 3.3333333333333335 = 4 - количество страниц
page = 4
limit = 3
start = (4-1) * 3 = 9
end = 3 * 3 = 9
page - номер страницы
limit - количество объектов на странице
start - индекс первого объекта на странице
end - индекс последнего объекта на странице
list[start:end] - срез списка, который содержит объекты на странице
query parameters - параметры запроса.
Параметры запроса - это часть URL, которая начинается с ? и содержит пары ключ=значение, разделенные &.
'''

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
from django.conf import settings

from product.models import Product, Category, Review
from product.forms import ProductCreateForm, ProductCreateForm2, CategoryCreateForm, ReviewCreateForm


def main_view(request):
    if request.method == 'GET':  # GET - получение данных
        return render(request, 'index.html')


def product_list_view(request):
    if request.method == 'GET':
        # 1 - получить все посты из базы данных
        products = Product.objects.all()  # QuerySet

        search = request.GET.get('search')
        order = request.GET.get('order')

        if search:
            # posts = posts.filter(title__icontains=search) | posts.filter(text__icontains=search)
            # | - оператор ИЛИ (OR)
            # & - оператор И (AND)
            products = products.filter(
                Q(title__icontains=search) | Q(text__icontains=search)
            )

        if order == 'date':
            products = products.order_by('created_at')

        if order == '-date':
            products = products.order_by('-created_at')

        if order == 'grade':
            products = products.order_by('grade')

        max_page = products.__len__() / settings.OBJECT_PER_PAGE

        # 105 / 10 = 10.5 = 11

        if round(max_page) < max_page:
            max_page += 1
        else:
            max_page = round(max_page)

        page = request.GET.get('page', 1)

        start = (int(page) - 1) * settings.OBJECT_PER_PAGE
        end = int(page) * settings.OBJECT_PER_PAGE

        # Formula:
        # start = (page - 1) * limit
        # end = page * limit

        # posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10]

        # example 1:
        # page = 1
        # limit = 3
        # start = (1-1) * 3 = 0
        # end = 1 * 3 = 3
        # posts[start:end] = [post1, post2, post3]

        # example 2:
        # page = 2
        # limit = 3
        # start = (2-1) * 3 = 3
        # end = 2 * 3 = 6
        # posts[start:end] = [post4, post5, post6]

        # example 3:
        # page = 3
        # limit = 3
        # start = (3-1) * 3 = 6
        # end = 3 * 3 = 9
        # posts[start:end] = [post7, post8, post9]

        # example 4:
        # page = 4
        # limit = 3
        # start = (4-1) * 3 = 9
        # end = 4 * 3 = 12
        # posts[start:end] = [post10]

        # 2 - передать посты в шаблон
        context = {
            'products': products[start:end],
            'max_page': range(1, int(max_page) + 1),
        }

        # 3 - вернуть ответ с шаблоном и данными
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


def product_update_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, '404.html')

    if request.method == 'GET':
        context = {
            'form': ProductCreateForm2(instance=product),
            'product': product,
        }
        return render(request, 'product/update.html', context=context)

    if request.method == 'POST':
        form = ProductCreateForm2(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect('/products/')
        else:
            context = {
                'form': form,
                'product': product,
            }
            return render(request, 'product/update.html', context=context)


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


def review_create_view(request, product_id):
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, '404.html')

        if form.is_valid():
            review = form.save(commit=False)
            review.product_id = product_id
            review.save()

            return redirect(f'/products/{product_id}/')
        else:
            context = {
                'product': product,
                'form': form,
            }

            return render(request, 'product/detail.html', context=context)
