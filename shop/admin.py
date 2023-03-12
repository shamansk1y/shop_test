from django.contrib import admin
from .models import Product, RecommendedProduct


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

