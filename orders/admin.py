from django.contrib import admin

from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "ordered", "status", ]


admin.site.register(Order, OrderAdmin)
