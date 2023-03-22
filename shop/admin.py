from django.contrib import admin
from .models import Product, RecommendedProduct, Category, Manufacturer, SubCategory, Size


class SizeInline(admin.TabularInline):
    model = Product.sizes.through

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price', 'available', 'manufacturer', 'category', 'status']
    list_filter = ['available', 'manufacturer', 'category', 'characteristics_gender', 'status', 'created', 'updated']
    list_editable = ['image', 'price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    inlines = [SizeInline]

class ProductInline(admin.TabularInline):
    model = Product
    fields = ['name', 'image', 'price', 'available', 'manufacturer', 'status']
    readonly_fields = ['name', 'image', 'price', 'available', 'manufacturer', 'status']
    can_delete = False
    extra = 0

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Розмірна сітка'
@admin.register(RecommendedProduct)
class RecommendedProduct(admin.ModelAdmin):
    model = RecommendedProduct
    list_filter = ['position']



class SubcategoryInline(admin.StackedInline):
    model = Category
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


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']
    inlines = [ProductInline]
