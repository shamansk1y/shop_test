from django.contrib import admin
from .models import Product, RecommendedProduct, Category, Manufacturer


class SubProdAdmin(admin.TabularInline):
    model = Product
    raw_id_fields = ['category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price', 'available', 'description', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['image', 'description', 'price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(RecommendedProduct)
class RecommendedProduct(admin.ModelAdmin):
    model = RecommendedProduct
    list_filter = ['position']


class SubcategoryInline(admin.TabularInline):
    model = Category
    fields = ['name', 'slug', 'position', 'is_visible']
    list_display_links = ['name']
    extra = 0
    verbose_name_plural = 'Підкатегорії'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','position', 'is_visible']
    list_editable = ['position', 'is_visible']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['parent']
    inlines = [SubcategoryInline]

    def parent_name(self, obj):
        if obj.parent:
            return obj.parent.name
        return ''
    parent_name.short_description = 'Материнська категорія'
    parent_name.admin_order_field = 'parent__name'

    def product_count(self, obj):
        return obj.product_set.count()
    product_count.short_description = 'Товарів'


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(parent__isnull=True)
        return qs


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    model = Manufacturer
    prepopulated_fields = {'slug': ('title',)}


