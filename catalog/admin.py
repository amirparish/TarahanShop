from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_featured', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['is_featured', 'category']
    ordering = ['-created_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)