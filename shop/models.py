from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from main_page.utils import get_file_name


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])


class RecommendedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'Рекомендовані товари'

    def __str__(self):
        return self.product.name



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

    def __str__(self):
        return self.name
