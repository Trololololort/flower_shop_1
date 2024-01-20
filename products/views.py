from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from products.models import Product


class ProductDetailView(DetailView):
    model = Product


