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
    context = {'form': search_bar,
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
            exat_product = Product.objects.get(pr_name__icontains=get_product)

            return redirect(f"product/{exat_product.id}")
        except:
            return redirect('/product-not-found')


# Если продукт не был найден
def pr_not_found(request):
    return render(request, 'not_found.html')


# Добавление товара в корзину
def add_to_cart(request, pk):
    if request.method == 'POST':
        cheker = Product.objects.get(id=pk)
        if cheker.pr_count >= int(request.POST.get('pr_amount')):
            Cart.objects.create(user_id=request.user.id,
                                user_pruduct=cheker,
                                user_product_quantity=int(request.POST.get('pr_amount'))).save()
            return redirect('/')


# Отображение корзина пользователя
def get_user_cart(request):
    # Вся инфао корзине пользователя
    cart = Cart.objects.filter(user_id=request.user.id)

    # Отправить данные на фронт
    context = {'cart':cart}
    return render(request, 'cart.html', context)


#Удаление товара из корзины
def del_from_cart(request, pk):
    product_to_delete = Product.objects.get(id=pk)
    Cart.objects.filter(user_id=request.user.id,
                        user_product=product_to_delete).delete()
    return redirect('/cart')