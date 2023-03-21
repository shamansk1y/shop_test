from django.shortcuts import get_object_or_404, render
from cart.cart import Cart
from main_page.context_data import get_common_context
from .models import Product
from django.core.paginator import Paginator



def product_list(request, category_slug=None):
    cart = Cart(request)
    products = Product.objects.filter(available=True).order_by('position')
    count = int(request.GET.get('count', 24)) # 24 это количество товаров по умолчанию
    paginator = Paginator(products, count) # разбиваем на страницы по count товаров на странице
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



def product_detail(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    data = {
        'product': product,
        'cart': cart,
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'detail.html', context=data)


