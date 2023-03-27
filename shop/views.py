from django.db.models import Avg, Q
from django.shortcuts import get_object_or_404, render, redirect
from cart.cart import Cart
from main_page.context_data import get_common_context, get_page_context
from main_page.forms import ReviewForm
from main_page.models import Review
from .models import Product, Manufacturer, Size
from django.core.paginator import Paginator


def product_list(request, category_slug=None):
    cart = Cart(request)
    sort = request.GET.get('sort', '')  # get sorting parameter
    products = Product.objects.filter(available=True)  # get all products

    # sort products
    if sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'date_desc':
        products = products.order_by('-created')
    else:
        products = products.order_by('position')

    # get price ranges
    price_ranges = [
        {'name': 'від 0 до 500 UAH', 'min': 0, 'max': 500},
        {'name': 'від 500 UAH до 1000 UAH', 'min': 500, 'max': 1000},
        {'name': 'від 1000 UAH до 1500 UAH', 'min': 1000, 'max': 1500},
        {'name': 'від 1500 UAH до 2000 UAH', 'min': 1500, 'max': 2000},
        {'name': 'від 2000 та вище', 'min': 2000, 'max': 9999},
    ]

    # get manufacturers
    manufacturers = Manufacturer.objects.all()

    # get selected manufacturers
    manufacturer_filters = request.GET.getlist('manufacturer_filter')

    # filter products by selected manufacturers
    if manufacturer_filters:
        products = products.filter(manufacturer__id__in=manufacturer_filters)

    # get all sizes
    sizes = Size.objects.all()

    # get selected sizes
    size_filters = request.GET.getlist('size_filter')

    # filter products by selected sizes
    if size_filters:
        products = products.filter(sizes__id__in=size_filters)

    # filter products by selected price range
    price_filters = request.GET.getlist('price_filter')
    if price_filters:
        price_query = Q()
        for price_filter in price_filters:
            min_price, max_price = price_filter.split('-')
            if max_price:
                price_query |= Q(price__gte=min_price, price__lte=max_price)
            else:
                price_query |= Q(price__gte=min_price)
        products = products.filter(price_query)

    count = int(request.GET.get('count', 24))
    paginator = Paginator(products, count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'products': page_obj,
        'cart': cart,
        'page_obj': page_obj,
        'price_ranges': price_ranges,
        'price_filters': price_filters,
        'manufacturers': manufacturers,
        'manufacturer_filters': manufacturer_filters,
        'sizes': sizes,
        'size_filters': size_filters,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'product_list.html', context=data)


def product_detail(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug, available=True)
    sizes = product.get_sizes()
    average_rating = Review.objects.aggregate(Avg('rating'))['rating__avg']
    review_app = product.review_set.filter(is_approved=True)
    data = {
        'product': product,
        'cart': cart,
        'sizes': sizes,
        'average_rating': average_rating,
        'review_app': review_app,
    }
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
    else:
        form = ReviewForm()
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    data['form'] = form
    return render(request, 'detail.html', context=data)