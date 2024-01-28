from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    exclude = [] # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.exclude
    list_display = ["id", "name", "color", "stock", ] # list_display


admin.site.register(Product, ProductAdmin)
