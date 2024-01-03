from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.forms import RegisterForm, AuthForm


def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm,
        }

        return render(request, 'user/register.html', context=context)

    elif request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            User.objects.create_user(

                username=form.cleaned_data.get('username'),

                email=form.cleaned_data.get('email'),

                first_name=form.cleaned_data.get('first_name'),

                last_name=form.cleaned_data.get('last_name'),

                password=form.cleaned_data.get('password'),

            )

            return redirect('/auth/login/')

        else:

            context = {

                'form': form,

            }

            return render(request, 'user/register.html', context=context)


def auth_view(request):
    if request.method == 'GET':
        context = {
            'form': AuthForm,
        }
        print(request.user)  # request.user - объект пользователя, который сделал запрос
        return render(request, 'user/auth.html', context=context)

    elif request.method == 'POST':
        form = AuthForm(request.POST)

        if form.is_valid():
            user = authenticate(**form.cleaned_data)  # метод который проверяет есть ли такой пользователь в базе данных

            if user is not None:
                login(request, user)  # метод который авторизует пользователя (создает сессию)
                return redirect('/products/')

            else:
                form.add_error(
                    None,
                    'Пользователь с такими данными не найден!'
                )

        return render(request, 'user/auth.html', context={'form': form})


def logout_view(request):
    logout(request)  # метод который разлогинивает пользователя (удаляет сессию)
    return redirect('/products/')


def profile_view(request):
    if request.method == 'GET':
        context = {
            'user': request.user,
        }

        return render(request, 'user/profile.html', context=context)


def delete_profile_view(request):
    if request.method == 'GET':
        request.user.delete()
        return redirect('/products/')
