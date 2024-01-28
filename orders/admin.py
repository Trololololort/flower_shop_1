from django.contrib import admin

from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    exclude = []
    list_filter = ["status"] # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/filters/#modeladmin-list-filters
    list_display = ["id", "ordered_at", "ordered_by", "status", "number_of_ordered_products", ] # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
                                                                                                # Методы можно использовать list_display (у нас это ordered_by, number_of_ordered_products).

# https://docs.djangoproject.com/en/5.0/intro/tutorial07/#customize-the-admin-form
admin.site.register(Order, OrderAdmin)
