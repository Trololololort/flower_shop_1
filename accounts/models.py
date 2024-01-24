from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    partonymic = models.CharField(max_length=100, blank=False, verbose_name="Отчество")
    rules = models.BooleanField(verbose_name="Согласен с правилами регистрации",
                                blank=False,
                                null=False,
                                default=False,
                                )