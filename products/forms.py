from django import forms

from products.const import SORT_CHOICES
from products.models import Product

class ProductSortFilterForm(forms.ModelForm):
    """
    В Django есть ModelForm: из модели делается форма.
    И особенностью является то, что если встретился в модели внешний ключ,
    то выпадающий список вариантов будет для нас подготовлен средствами Django
    из коробки. Так экономим время: иначе бы пришлось выбор категорий писать вручную.

    Поэтому берем модель Product. Она большая, а нам нужно из нее только категория.
    Поэтому fields = ["category"].

    Категория у товара в модели - обязательна к заполнению. А в форме - не обязательна.
    Поэтому так объявляем, для чего переопределим конструктор формы.

    Так как в модели Product ничего не было про сортировку, добавим поле order_by.

    Документация:
    1) https://docs.djangoproject.com/en/5.0/ref/forms/fields/#choicefield
    2) https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].required = False

    # https://docs.djangoproject.com/en/5.0/ref/forms/fields/#choicefield
    order_by = forms.ChoiceField(choices=SORT_CHOICES, label="Сортировать по", required=False)

    class Meta:
        model = Product
        fields = ["category"]
        labels = {
            "category": "Фильтр"
        }
