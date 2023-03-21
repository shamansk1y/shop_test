from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from main_page.context_data import get_page_context, get_common_context
from main_page.forms import ContactUsForm, SubscriptionForm
from shop.models import Category, Product


def handle_post_request(request):

    contact_us = ContactUsForm(request.POST)
    subscription = SubscriptionForm(request.POST)

    if contact_us.is_valid():
        contact_us.save()
        return redirect('/')
    if subscription.is_valid():
        subscription.save()
        return redirect('/')



def index(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'index.html', context=data)

def contacts(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'contact.html', context=data)


def category_list(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'category_list.html', context=data)


def sub_category_list(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    child = cat.children.all()
    cat_products = Product.objects.filter(category=cat)  # фильтруем товары по категории
    paginator = Paginator(cat_products, 24) # разбиваем на страницы по 8 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'cat': cat,
        'child': child,
        'cat_products': cat_products,  # передаем отфильтрованные товары в шаблон
        'page_obj': page_obj,
    }
    context_data = get_common_context()
    data.update(context_data)
    if cat.is_parent():
        return render(request, 'sub_category_list.html', context=data)
    else:
        return render(request, 'sub_category_product_list.html', context=data)

def search(request):
    query = request.GET.get('q')
    search_products = Product.objects.filter(name__icontains=query)
    data = {'search_products': search_products, 'query': query}
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'search.html', context=data)
