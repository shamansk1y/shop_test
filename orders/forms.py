from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    DELIVERY_CHOICES = (
        ('pickup', 'Самовывоз'),
        ('address', 'Адресная доставка'),
    )

    delivery_option = forms.ChoiceField(choices=DELIVERY_CHOICES, widget=forms.RadioSelect)

    PAYMENT_CHOICES = (
        ('pay_after_take', 'Оплата при отриманні'),
        ('bank_card', 'Оплата на карту банка'),
        ('bank_accoun', 'Безготівкой розрахунок(ФОП/ТОВ)'),
        ('cash', 'Готівкою* (*лише за умови самовивозу з магазину)'),

    )
    payment_option = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Order
        fields = ['last_name', 'first_name', 'delivery_option', 'address', 'payment_option']
