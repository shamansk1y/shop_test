import os
from io import BytesIO
from ckeditor.fields import RichTextField
from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from main_page.utils import get_file_name
from PIL import Image
from django.utils import timezone


class Size(models.Model):
    name = models.CharField(max_length=50)
    position = models.IntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Розмірна сітка'


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
        # проверяем, есть ли изображение
        if self.photo:
            # открываем изображение с помощью библиотеки PIL
            img = Image.open(self.photo)

            # проверяем, является ли изображение квадратным
            if img.width != img.height:
                size = (max(img.width, img.height), max(img.width, img.height))
                img_with_border = Image.new("RGB", size, (245, 245, 245))
                x = (size[0] - img.width) // 2
                y = (size[1] - img.height) // 2
                img_with_border.paste(img, (x, y))

                # получаем формат изображения из имени файла
                file_ext = os.path.splitext(self.photo.name)[1].lower()
                format_dict = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.png': 'PNG', '.gif': 'GIF'}
                image_format = format_dict.get(file_ext, 'JPEG')

                # сохраняем квадратное изображение в том же формате, что и оригинал
                img_io = BytesIO()
                img_with_border.save(img_io, format=image_format)
                img_io.seek(0)
                self.photo.save(self.photo.name, ContentFile(img_io.read()), save=False)


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

class SubCategory(Category):
    class Meta:
        proxy = True
        verbose_name = 'Підкатегорія'
        verbose_name_plural = 'Підкатегорії'

    def save(self, *args, **kwargs):
        if self.parent is None:
            raise ValueError('SubCategory must have a parent')
        super(SubCategory, self).save(*args, **kwargs)


class Manufacturer(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to=get_file_name)
    grid_image = models.ImageField(upload_to=get_file_name, blank=True)
    position = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)
    description = RichTextField()
    h1 = models.CharField(max_length=255, blank=True)
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.CharField(max_length=255, blank=True)

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

        super(Manufacturer, self).save(*args, **kwargs)

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
    position = models.PositiveIntegerField(default=1)
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
    sizes = models.ManyToManyField(Size, related_name='products', blank=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'Товари'

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.slug])

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

    def get_sizes(self):
        return self.sizes.filter(is_visible=True)

    def get_subproductimages(self):
        return self.subproductimages.all()

    def __str__(self):
        return self.name

class SubProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subproductimages')
    image = models.ImageField(upload_to=get_file_name, blank=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product.slug)
        # проверяем, есть ли изображение с таким же slug
        i = 1
        while SubProductImage.objects.filter(product=self.product, slug=self.slug).exists():
            i += 1
            self.slug = f"{slugify(self.product.slug)}-{i}"
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


        super(SubProductImage, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Дополнительные изображения товара'

    def __str__(self):
        return f'{self.product.name} - {self.id}'



class RecommendedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'Рекомендовані товари'

    def __str__(self):
        return self.product.name


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    products = models.ManyToManyField(Product, blank=True)
    exclude_manufacturers = models.ManyToManyField(Manufacturer, blank=True, related_name='excluded_coupons')
    exclude_categories = models.ManyToManyField(Category, blank=True, related_name='excluded_coupons')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    uses_remaining = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    def can_be_used(self):
        return self.status and self.start_date <= timezone.now() <= self.end_date and self.uses_remaining > 0

    def is_valid_product(self, product):
        if self.products.exists() and product not in self.products.all():
            return False
        if self.exclude_manufacturers.exists() and product.manufacturer in self.exclude_manufacturers.all():
            return False
        if self.exclude_categories.exists() and product.category in self.exclude_categories.all():
            return False
        return True

    def apply_discount(self, cart):
        if not self.can_be_used():
            return
        for item in cart:
            if self.is_valid_product(item['product']):
                item['total_price'] -= item['price'] * self.discount
        self.uses_remaining -= 1
        if self.uses_remaining == 0:
            self.status = False
        self.save()

    class Meta:
        ordering = ['-end_date']
        verbose_name_plural = 'Купони на знижку'