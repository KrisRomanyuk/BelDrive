from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Помощь", 'url_name': 'helpme'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Авторизация", 'url_name': 'login'}
        ]


def index(request):
    posts = Fines.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }

    return render(request, 'myfines/index.html', context=context)


def about(request):
    return render(request, 'myfines/about.html', {'menu': menu, 'title': 'О сайте'})


def helpme(request):
    return HttpResponse("Помощь")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
