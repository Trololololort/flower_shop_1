from django.contrib import admin

from selected_products.models import SelectedProduct


class CartAdmin(admin.ModelAdmin):
    exclude = [] # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.exclude
    list_display = ["id", "user", "order", "product", "price", "quantity", ] # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display


admin.site.register(SelectedProduct, CartAdmin)
