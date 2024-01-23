from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "name", "color", "stock", ]


admin.site.register(Product, ProductAdmin)
