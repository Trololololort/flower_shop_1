from django.contrib import admin

from selected_products.models import SelectedProduct


class CartAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "user", "order", "product", "price", "quantity", ]


admin.site.register(SelectedProduct, CartAdmin)
