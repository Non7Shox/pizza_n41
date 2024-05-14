from django.contrib import admin
from products.models import ProductModel, CategoryModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('name', 'description',)


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('name',)
