
# https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices
# Будет применяться в CharField.
ORDER_STATUS = [
    ("NEW", "Новый"),
    ("CONFIRMED", "Подтвержден"),
    ("CANCELLED", "Отменен"),
]