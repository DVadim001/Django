from django.shortcuts import render
from . import forms
# Create your views here.


# отображение главной статраницы
def home(request):
    search_bar = forms.SearchForm()
    # отправить элементы нафронт
    context = {'form':search_bar}
    return render(request, 'home.html', context)


# отображение страницы о нас
def about(request):
    return render(request, 'about.html')


# отображение страницы с контактами
def contact(request):
    return render(request, 'contact.html')


# поиск продукта
def search_product(request):
    if request.method == 'POST':
        pass
