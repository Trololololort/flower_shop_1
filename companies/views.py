from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import Product


class AboutCompanyView(TemplateView): # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview
    template_name = "companies/about.html" # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview

    def get_context_data(self, **kwargs): # # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview
        """
        По ТЗ надо отобразить слайдер. Поэтому делаем запрос в базу данных,
        результат передаем в контекст.
        """

        context = super().get_context_data(**kwargs)
        context["object_list"] = Product.in_stock.all()[:5] # Применен менеджер in_stock (см. к нему комментарий).
                                                            # https://docs.djangoproject.com/en/5.0/topics/db/queries/#limiting-querysets
        return context

class ContactsView(TemplateView): # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview
    template_name = "companies/contacts.html" # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview