from django import forms


class PasswordField(forms.CharField):
    widget = forms.PasswordInput # https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#passwordinput

class OrderForm(forms.Form):
    password = PasswordField(label="Пароль")
