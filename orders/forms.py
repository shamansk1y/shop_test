from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "Вкажіть Ваше прізвище",
    }))

    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "Вкажіть Ваше ім'я",
    }))

    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "example@email.com",
    }))

    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "380991234567",
    }))

    city = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "Ваш населенний пункт",
    }))

    postal_code = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "123",
    }))

    address = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "вулиця/будинок/квартира",
    }))

    message = forms.CharField(max_length=250, required=False, widget=forms.Textarea(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "Додаткова інформація - не обов'язково",
    }))

    DELIVERY_CHOICES = (
        ('devivery_post', 'Відправка на відділення/поштомат Нової Пошти'),
        ('pickup', 'Самовивіз з магазину'),
        ('address', "Адресна доставка кур'єрською служною Нова Пошта"),
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
        fields = ['last_name', 'first_name', 'email', 'phone', 'message', 'city', 'postal_code', 'delivery_option',
                  'address', 'payment_option']
