from django import forms


class OrderForm(forms.Form):
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(widget=forms.PasswordInput()),
    )