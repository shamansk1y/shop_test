from django.db import models
from main_page.utils import get_file_name


class Slider(models.Model):

    title = models.CharField(max_length=50, verbose_name="Назва слайду")
    position = models.SmallIntegerField(verbose_name="Позиція")
    image = models.ImageField(upload_to=get_file_name, verbose_name="Зображення")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    h_1 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок")
    desc = models.TextField(max_length=500, blank=True, verbose_name="Опис")
    tab = models.CharField(max_length=50, blank=True, verbose_name="Текст кнопки")
    tab_url = models.URLField(blank=True, verbose_name="Посилання з кнопки")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Слайдер'


class Baner(models.Model):
    title = models.CharField(max_length=50, verbose_name="Назва слайду")
    position = models.SmallIntegerField(verbose_name="Позиція")
    image_1 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення банер 1")
    h_1 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок банер 1")
    desc_1 = models.TextField(max_length=500, blank=True, verbose_name="Опис банер 1")
    tab_1 = models.CharField(max_length=50, blank=True, verbose_name="Текст кнопки банер 1")
    tab_url_1 = models.URLField(blank=True, verbose_name="Посилання з кнопки банер 1")
    image_2 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення банер 2")
    h_2 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок банер 2")
    desc_2 = models.TextField(max_length=500, blank=True, verbose_name="Опис банер 2")
    tab_2 = models.CharField(max_length=50, blank=True, verbose_name="Текст кнопки банер 2")
    tab_url_2 = models.URLField(blank=True, verbose_name="Посилання з кнопки банер 2")
    image_3 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення банер 3")
    h_3 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок банер 3")
    desc_3 = models.TextField(max_length=500, blank=True, verbose_name="Опис банер 3")
    tab_3 = models.CharField(max_length=50, blank=True, verbose_name="Текст кнопки банер 3")
    tab_url_3 = models.URLField(blank=True, verbose_name="Посилання з кнопки банер 3")
    image_4 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення банер 4")
    h_4 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок банер 4")
    desc_4 = models.TextField(max_length=500, blank=True, verbose_name="Опис банер 4")
    tab_4 = models.CharField(max_length=50, blank=True, verbose_name="Текст кнопки банер 4")
    tab_url_4 = models.URLField(blank=True, verbose_name="Посилання з кнопки банер 4")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Банер'


class Advantages(models.Model):

    title = models.CharField(max_length=50, verbose_name="Назва")
    position = models.SmallIntegerField(verbose_name="Позиція")
    h_1 = models.CharField(max_length=50, blank=True, verbose_name="Заголовок 1")
    h_2 = models.CharField(max_length=50, blank=True, verbose_name="Заголовок 2")
    h_3 = models.CharField(max_length=50, blank=True, verbose_name="Заголовок 3")
    h_4 = models.CharField(max_length=50, blank=True, verbose_name="Заголовок 4")


    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Переваги головна'



class Contacts(models.Model):

    address = models.CharField(max_length=70, verbose_name="Адреса")
    phone_1 = models.CharField(blank=True, max_length=50, verbose_name="Телефон 1")
    phone_2 = models.CharField(blank=True, max_length=50, verbose_name="Телефон 2")
    phone_3 = models.CharField(blank=True, max_length=50, verbose_name="Телефон 3")
    email = models.CharField(max_length=50, verbose_name="Пошта ")
    day_open = models.CharField(blank=True, max_length=50, verbose_name="Робочі дні")
    hours_of_work = models.CharField(blank=True, max_length=50, verbose_name="Робочі години")
    weekend_work = models.CharField(blank=True, max_length=50, verbose_name="Робота в вихідні")
    weekend_hours_of_work = models.CharField(blank=True, max_length=50, verbose_name="Робочі години в вихідні")
    fb_url = models.URLField(blank=True, verbose_name="Посилання на facebook", default='https://www.facebook.com/')
    youtube_url = models.URLField(blank=True, verbose_name="Посилання на youtube", default='https://www.youtube.com/')
    in_url = models.URLField(blank=True, verbose_name="Посилання на instagram", default='https://www.instagram.com/')

    def __str__(self):
        return f'{self.address}'

    class Meta:
        ordering = ('address',)
        verbose_name_plural = 'Контакти'


class Subscription(models.Model):

    email = models.EmailField()
    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'Підписка на email розсилку'


class ContactUs(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=250, blank=True)
    subject = models.CharField(max_length=50)

    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = "Зворотній зв'язок"