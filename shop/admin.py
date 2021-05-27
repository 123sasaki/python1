from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available']
    list_editable = ['price', 'stock', 'available']
    prepopulated_field = {'slug':('name',)}
admin.site.register(Product, ProductAdmin)
