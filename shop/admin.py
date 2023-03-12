from django.contrib import admin
from .models import Product, RecommendedProduct, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'description', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['description', 'price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(RecommendedProduct)
class RecommendedProduct(admin.ModelAdmin):
    model = RecommendedProduct
    list_filter = ['position']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'photo', 'position', 'is_visible', 'parent']
    list_filter = ['name', 'slug', 'photo', 'position', 'is_visible', 'parent']
    list_editable = ['slug', 'photo', 'position', 'is_visible', 'parent']
    prepopulated_fields = {'slug': ('name',)}


