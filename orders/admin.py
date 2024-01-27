from django.contrib import admin

from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    exclude = []
    list_filter = ["status"]
    list_display = ["id", "ordered_at", "ordered_by", "status", "number_of_ordered_products", ]


admin.site.register(Order, OrderAdmin)
