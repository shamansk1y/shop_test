"""
Module containing functions related to obtaining page context.
Functions:
- get_common_context: gets the common page context used across multiple pages of the site.
- get_page_context: gets the page context with the current request taken into account.
"""


from .forms import SubscriptionForm, ContactUsForm
from .models import Slider, Baner, Advantages, Contacts
from shop.models import Product, RecommendedProduct, Category, Manufacturer

def get_common_context():
    return {
        'slider': Slider.objects.filter(is_visible=True),
        'baner': Baner.objects.get(id=1),
        'advantages': Advantages.objects.get(id=1),
        'contacts': Contacts.objects.get(id=1),
        'subscription': SubscriptionForm(),
        'contact_us': ContactUsForm(),
        'last_products': Product.objects.order_by('-created')[:8],
        'products': Product.objects.filter(available=True),
        'recommended_products': RecommendedProduct.objects.all()[:8],
        'category': Category.objects.filter(parent=None),
        'manufacturer': Manufacturer.objects.all(),
    }


def get_page_context(request):
    """
    Gets the page context with the current request taken into account.
    Args:
    - request: HttpRequest object.
    Returns:
    - tuple of two elements:
        - dictionary containing data specific to the current request:
            'user_manager': True if the user is in the 'manager' group, False otherwise.
            'user_auth': True if the user is authenticated, False otherwise.
        - dictionary containing the common page context obtained from the get_common_context function.
    """
    data = {
        'user_manager': request.user.groups.filter(name='manager').exists(),
        'user_auth': request.user.is_authenticated,
    }
    context = get_common_context()
    data.update(context)
    return data