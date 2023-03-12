from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Назва', max_length=255)
    h1 = forms.CharField(label='H1', max_length=255)
    description = forms.CharField(label='Опис', widget=forms.Textarea)
    photo = forms.ImageField(label='Фото', required=False)
    meta_title = forms.CharField(label='Мета-тег Title', max_length=255)
    meta_description = forms.CharField(label='Мета-тег Description', max_length=255)
    position = forms.IntegerField(label='Позиція', required=False)
    is_visible = forms.BooleanField(label='Показувати на сайті на сайте', required=False)
    parent = forms.ModelChoiceField(label='Материнська категорія', queryset=Category.objects.filter(parent__isnull=True), required=False)

    class Meta:
        model = Category
        fields = ('name', 'h1', 'description', 'photo', 'meta_title', 'meta_description', 'position', 'is_visible', 'parent')
