from decimal import Decimal

from django.conf import settings

from shop.models import Product

class Cart:

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False, size=None):
        """
        Add a product to the cart or update its quantity.
        """
        key = str(product.id) + '-' + str(size) if size else str(product.id)
        if key not in self.cart:
            if product.discounted_price:
                self.cart[key] = {'quantity': 0, 'price': str(product.discounted_price), 'size': size}
            else:
                self.cart[key] = {'quantity': 0, 'price': str(product.price), 'size': size}
        if update_quantity:
            self.cart[key]['quantity'] = quantity
        else:
            self.cart[key]['quantity'] += quantity
        self.save()

    def add_quantity(self, product, size=None):
        key = str(product.id) + '-' + str(size) if size else str(product.id)
        if key in self.cart:
            self.cart[key]['quantity'] += 1
            self.save()


    def sub(self, product, size=None):
        key = str(product.id) + '-' + str(size) if size else str(product.id)
        if key in self.cart:
            self.cart[key]['quantity'] -= 1
            if self.cart[key]['quantity'] <= 0:
                del self.cart[key]
            self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product, size=None):
        key = str(product.id) + '-' + str(size) if size else str(product.id)
        if key in self.cart:
            del self.cart[key]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        product_ids = [key.split('-')[0] for key in self.cart.keys()]
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            for key in cart.keys():
                if str(product.id) == key.split('-')[0]:
                    if not cart[key].get('product'):
                        cart[key]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())