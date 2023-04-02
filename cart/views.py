from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET
from main_page.context_data import get_common_context, get_page_context
from shop.models import Product, Coupon
from .cart import Cart


@require_GET
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    size = request.GET.get('size')
    cart.add(product=product, quantity=1, update_quantity=False, size=size)
    return redirect('cart:cart_detail')

@require_GET
def cart_remove(request, product_id, size):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product, size=size)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    data = {'cart': cart}
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'cart_detail.html', context=data)

@require_GET
def cart_sub(request, product_id, size):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.sub(product=product, size=size)
    return redirect('cart:cart_detail')

@require_GET
def cart_add_quantity(request, product_id, size):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add_quantity(product=product, size=size)
    return redirect('cart:cart_detail')