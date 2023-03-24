from django.shortcuts import get_object_or_404, render
from cart.cart import Cart
from main_page.context_data import get_common_context
from .models import Product
from django.core.paginator import Paginator


def product_list(request, category_slug=None):
    cart = Cart(request)
    sort = request.GET.get('sort', '')  # получаем параметр сортировки
    products = Product.objects.filter(available=True)  # получаем все продукты

    # обработка сортировки
    if sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'date_desc':
        products = products.order_by('-created')
    else:
        products = products.order_by('position')

    count = int(request.GET.get('count', 24))
    paginator = Paginator(products, count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'products': products,
        'cart': cart,
        'page_obj': page_obj,
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'product_list.html', context=data)


def product_detail(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug, available=True)
    sizes = product.get_sizes()
    data = {
        'product': product,
        'cart': cart,
        'sizes': sizes,
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'detail.html', context=data)


