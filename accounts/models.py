from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    """
    В Django можно изменить модель User двумя способами:
    1. https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#extending-the-existing-user-model
    2. https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#substituting-a-custom-user-model

    В данном случае выбран второй способ. Подошел бы и первый, но
    "it’s highly recommended to set up a custom user model".
    Т.е. судя по документации, рекомендуется второй способ.
    """

    patronymic = models.CharField(max_length=100, blank=False, verbose_name="Отчество") # https://docs.djangoproject.com/en/5.0/ref/forms/fields/#charfield


    """
    Видимо, можно было бы не заводить в модели специальное поле для
    согласия с правилами. Но удобно его завести: оно в шаблонах отобразится сразу.
    
    А в реальном проекте обязательно надо сохранять информацию, что пользователь
    согласился с правилами. Это юридически значимая информация. 
    """
    rules = models.BooleanField(verbose_name="Согласен с правилами регистрации",
                                blank=False,
                                null=False,
                                default=False,
                                )

    @property
    def full_name(self):
        """
        Для админки. По ТЗ в списке заказов видно ФИО заказчика.
        """
        return "{} {} {}".format(self.last_name, self.patronymic, self.last_name)