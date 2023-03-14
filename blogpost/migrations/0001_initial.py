# Generated by Django 4.1.7 on 2023-03-14 16:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0005_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d/')),
                ('position', models.IntegerField(default=0)),
                ('content', ckeditor.fields.RichTextField()),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=255, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('blog_products', models.ManyToManyField(blank=True, to='shop.product')),
            ],
            options={
                'verbose_name_plural': 'Блог',
                'ordering': ('-pub_date',),
            },
        ),
    ]
