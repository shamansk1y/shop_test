from django.db.models import Avg
from django.shortcuts import get_object_or_404, render, redirect
from cart.cart import Cart
from main_page.context_data import get_common_context
from main_page.forms import ReviewForm
from main_page.models import Review
from .models import Product, Manufacturer
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

    # получаем диапазоны цен
    price_ranges = [
        {'name': 'від 0 до 500 UAH', 'min': 0, 'max': 500},
        {'name': 'від 500 UAH до 1000 UAH', 'min': 500, 'max': 1000},
        {'name': 'від 1000 UAH до 1500 UAH', 'min': 1000, 'max': 1500},
        {'name': 'від 1500 UAH до 2000 UAH', 'min': 1500, 'max': 2000},
        {'name': 'від 2000 та вище', 'min': 2000, 'max': None},
    ]

    # получаем список производителей
    manufacturers = Manufacturer.objects.all()

    # получаем выбранные пользователем производители
    manufacturer_filters = request.GET.getlist('manufacturer_filter')

    # фильтруем продукты по выбранным производителям
    filtered_products = []

    for manufacturer in manufacturers:
        if str(manufacturer.id) in manufacturer_filters:
            filtered_products += products.filter(manufacturer=manufacturer)

    # если ни один производитель не выбран, то выводим все продукты
    if not manufacturer_filters:
        filtered_products = products

    # фильтр по цене (как в примере выше)
    price_filters = request.GET.getlist('price_filter')
    ...

    count = int(request.GET.get('count', 24))
    paginator = Paginator(filtered_products, count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # получаем количество продуктов в каждом диапазоне цен
    price_counts = []
    for price_range in price_ranges:
        count = 0
        for product in filtered_products:
            if price_range['max']:
                if price_range['min'] <= product.price < price_range['max']:
                    count += 1
            else:
                if price_range['min'] <= product.price:
                    count += 1
        price_counts.append({'name': price_range['name'], 'count': count})

    data = {
        'products': filtered_products,
        'cart': cart,
        'page_obj': page_obj,
        'price_ranges': price_ranges,
        'price_filters': price_filters,
        'price_counts': price_counts,
        'manufacturers': manufacturers,
        'manufacturer_filters': manufacturer_filters,
    }
    context_data = get_common_context()
    data.update(context_data)
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
    context_data = get_common_context()
    data.update(context_data)
    data['form'] = form
    return render(request, 'detail.html', context=data)