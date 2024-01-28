from django.db import models


class NameMixin(models.Model):
    name = models.CharField(max_length=100, # https://docs.djangoproject.com/en/5.0/ref/models/fields/#charfield
                            null=False,
                            blank=False,
                            default="",
                            verbose_name="Наименование")

    def __str__(self): # https://docs.djangoproject.com/en/5.0/ref/models/instances/#str
        return self.name

    class Meta:
        abstract = True # https://docs.djangoproject.com/en/5.0/ref/models/options/#abstract


class UserMixin(models.Model):
    user = models.ForeignKey("accounts.CustomUser", # https://docs.djangoproject.com/en/5.0/ref/models/fields/#foreignkey
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь", )


    class Meta:
        abstract = True # https://docs.djangoproject.com/en/5.0/ref/models/options/#abstract