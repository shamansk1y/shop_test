from django.core.validators import RegexValidator
from django.db import models
from shop.models import Product


class Order(models.Model):
    phone_validator = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[ -]?){7}$', message='Error phone number')

    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[phone_validator])
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    address = models.CharField(max_length=250, blank=True)
    message = models.TextField(max_length=250, blank=True)
    DELIVERY_CHOICES = (
        ('devivery_post', 'Відправка на відділення/поштомат Нової Пошти'),
        ('pickup', 'Самовивіз з магазину'),
        ('address', "Адресна доставка кур'єрською служною Нова Пошта"),
    )
    delivery_option = models.CharField(max_length=50, choices=DELIVERY_CHOICES)
    PAYMENT_CHOICES = (
        ('pay_after_take', 'Оплата при отриманні'),
        ('bank_card', 'Оплата на карту банка'),
        ('bank_accoun', 'Безготівкой розрахунок(ФОП/ТОВ)'),
        ('cash', 'Готівкою* (*лише за умови самовивозу з магазину)'),
    )
    payment_option = models.CharField(max_length=50, choices=PAYMENT_CHOICES)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=50, blank=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return 'f {}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity