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

    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "Ваш населенний пункт",
    }))

    postal_code = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "123",
    }))

    address = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "Ваша адреса - не обов'язково",
    }))

    message = forms.CharField(max_length=250, widget=forms.Textarea(attrs={
    'class': "form-control",
    'type': "text",
    'placeholder': "Додаткова інформація - не обов'язково",
    }))

    class Meta:
        model = Order
        fields = ['last_name', 'first_name', 'email', 'phone', 'city', 'postal_code', 'address', 'message']
