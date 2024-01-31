from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import News_article


# Отображение главной страницы (все новости)
def home(request):
    articles_news = News_article.objects.order_by('-news_date')[:5]
    return render(request, 'home.html', {'articles_news': articles_news})


# Страница О нас
def about(request):
    return render(request, 'about.html')


# Страница контактов
def contacts(request):
    return render(request, 'contacts.html')

# Страница одной новости
def article(request, pk):
    try:
        a = News_article.objects.get(id=pk)
    except:
        raise Http404('Новость не найдена.')
    comments = a.news_comment_set.order_by('-id')[:10]
    return render(request, 'article.html', {'news': a, 'comments':comments})


# Поиск новости
def search_article(request):
    return render(request, '')


# Новость не найдена
def article_not_found(request):
    return render(request, 'not_found.html')


# Оставление комментария
def comment(request, pk):
    try:
        a = News_article.objects.get(id=pk)
    except:
        raise Http404('Новость не найдена.')
    a.news_comment_set.create(comment_author=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('news:article', args=(a.id,)))
