from django.shortcuts import render
from . import forms


# Отображение главной страницы
def home(request):
    if request.method == "POST":
        pass

    # Создание объекта формы
    search = forms.SearchForm()


    # и передача его на фронтенд
    context = {'form': search}

    return render(request, 'home.html', context)


# Страница О нас
def about(request):
    return render(request, 'about.html')


# Страница контактов
def contacts(request):
    return render(request, 'contacts.html')

# Страница новости
def article(request):
    return render(request, 'article.html')


# Поиск новости
def search_article(request):
    return render(request, '')


# Новость не найдена
def article_not_found(request):
    return render(request, 'not_found.html')
