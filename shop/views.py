from django.shortcuts import get_object_or_404, render

from cart.cart import Cart
from main_page.context_data import get_common_context
from .models import Product


def product_list(request, category_slug=None):
    cart = Cart(request)
    products = Product.objects.filter(available=True)
    data = {
        'products': products,
        'cart': cart
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'product_list.html', context=data)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    data = {
        'product': product
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'detail.html', context=data)

