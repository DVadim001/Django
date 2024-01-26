from django.shortcuts import render, redirect
from . import forms
from .models import Product, Category, Cart
# Create your views here.


# отображение главной статраницы
def home(request):
    # Поисковая строка
    search_bar = forms.SearchForm()
    # Собираем все продукты
    product_info = Product.objects.all()
    # Собираем все категории товаров
    category_info = Category.objects.all()
    # отправить элементы на фронт
    context = {'form':search_bar,
               'product': product_info,
               'category': category_info}
    return render(request, 'home.html', context)


# Вывод товаров по определённой категории
def get_full_category(request, pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(category_name=category)
    # Отправляем данные на фронт
    context = {'products': products}
    return render(request, 'category.html', context)


# Вывод информации о конкретном продукте
def get_full_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'product.html', context)

# отображение страницы о нас
def about(request):
    return render(request, 'about.html')


# отображение страницы с контактами
def contact(request):
    return render(request, 'contact.html')


# поиск продукта
def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')

        try:
            exat_product = Product.objects.get(product_name__icontains=get_product)

            return redirect(f"pruduct/{exat_product.id}")
        except:
            return redirect('product-not-found')


# Если продукт не был найден
def pr_not_found(request):
    return render(request, 'not_found.html')