import os
from io import BytesIO
from ckeditor.fields import RichTextField
from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from main_page.utils import get_file_name
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='Слаг')
    h1 = models.CharField(max_length=255, verbose_name='H1', blank=True)
    description = models.TextField(verbose_name='Опис', blank=True)
    photo = models.ImageField(upload_to=get_file_name, verbose_name='Фото', blank=True, null=True)
    meta_title = models.CharField(max_length=255, verbose_name='Мета-тег Title', blank=True)
    meta_description = models.CharField(max_length=255, verbose_name='Мета-тег Description', blank=True)
    position = models.PositiveIntegerField(default=0, verbose_name='Позиція')
    is_visible = models.BooleanField(default=True, verbose_name='Показувати на сайті')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children',
                               verbose_name='Материнська категорія')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


    def get_absolute_url(self):
        return reverse("main_page:sub_category_list", args=[self.slug])

    def is_parent(self):
        return self.parent is None

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='manufacturer/images/')
    grid_image = models.ImageField(upload_to='manufacturer/grid_images/', blank=True)
    position = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)
    description = RichTextField()
    h1 = models.CharField(max_length=255, blank=True)
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Виробник'
        verbose_name_plural = 'Виробники'


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to=get_file_name, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    GENDER_CHOICES = [
        ('Ч', 'Чоловічий'),
        ('Ж', 'Жіночий'),
        ('Д', 'Дитячий'),
        ('П', 'Підлітковий'),
        ('У', 'Унісекс'),
        ]
    characteristics_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, default=True)
    STASTUS_CHOICES = [
        ('Н', 'Немає в наявності'),
        ('В', 'В наявності'),
        ('П', 'Під замовлення 2-3 дні'),
        ('З', 'Під замовлення 2-4 тижні'),
        ('C', 'Скоро в наявності'),
        ]
    status = models.CharField(max_length=1, choices=STASTUS_CHOICES, blank=True, default='Н')

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'Товари'

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        # проверяем, есть ли изображение
        if self.image:
            # открываем изображение с помощью библиотеки PIL
            img = Image.open(self.image)

            # проверяем, является ли изображение квадратным
            if img.width != img.height:
                size = (max(img.width, img.height), max(img.width, img.height))
                img_with_border = Image.new("RGB", size, (245, 245, 245))
                x = (size[0] - img.width) // 2
                y = (size[1] - img.height) // 2
                img_with_border.paste(img, (x, y))

                # получаем формат изображения из имени файла
                file_ext = os.path.splitext(self.image.name)[1].lower()
                format_dict = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.png': 'PNG', '.gif': 'GIF'}
                image_format = format_dict.get(file_ext, 'JPEG')

                # сохраняем квадратное изображение в том же формате, что и оригинал
                img_io = BytesIO()
                img_with_border.save(img_io, format=image_format)
                img_io.seek(0)
                self.image.save(self.image.name, ContentFile(img_io.read()), save=False)

        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.name



class RecommendedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'Рекомендовані товари'

    def __str__(self):
        return self.product.name





