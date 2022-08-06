from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = ['О сайте', 'Обратная связь', 'Помощь', 'Войти']


def index(request):
    posts = Fines.objects.all()
    return render(request, 'myfines/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'myfines/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)

    return HttpResponse(f'<h1>Архив по годам</h1>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
