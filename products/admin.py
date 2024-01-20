from django.contrib import admin

from products.models import Country, Category, Color, Product

admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Color)


class ProductAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "name", "color", "stock", ]


admin.site.register(Product, ProductAdmin)
