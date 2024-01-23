from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import Product


class AboutCompanyView(TemplateView):
    template_name = "companies/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Product.in_stock.all()[:5]
        return context

class ContactsView(TemplateView):
    template_name = "companies/contacts.html"