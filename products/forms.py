from django import forms

from products.const import SORT_CHOICES
from products.models import Product
from product_properties.models import Category


def get_choices():
    choices = [(k, v) for k, v in SORT_CHOICES.items()]
    return choices


class ProductSortFilterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].required = False

    order_by = forms.ChoiceField(choices=get_choices, label="Сортировать по", required=False)

    class Meta:
        model = Product
        fields = ["category"]
        labels = {
            "category": "Фильтр"
        }
