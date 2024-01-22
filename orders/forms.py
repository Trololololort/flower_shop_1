from django import forms


class PasswordField(forms.CharField):
    widget = forms.PasswordInput

class OrderForm(forms.Form):
    password = PasswordField()
