from django.shortcuts import render
from cart.cart import Cart
from main_page.context_data import get_common_context
from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'], size=item['size'])
            
            # clear the cart
            cart.clear()
            data = {'order': order}
            context_data = get_common_context()
            data.update(context_data)
            return render(request, 'created.html', context=data)
    else:
        form = OrderCreateForm()
    data = {'cart': cart, 'form': form}
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'create.html', context=data)
