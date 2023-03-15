from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class InfoPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='info_page/%Y/', null=True, blank=True)
    content = RichTextField()
    position = models.IntegerField(default=0)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.CharField(max_length=255, null=True, blank=True)


    def get_absolute_url(self):
        return reverse('info_page', args=[str(self.slug)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Інформаційні сторінки'