from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from accounts.const import FIELD_NAME_MAPPING, ValidationPatterns, SignUpErrorMessages
from accounts.models import CustomUser


class LoginForm(AuthenticationForm):
    """
    Самый простой способ соблюсти требования ТЗ -
    подменить имена полей в форме из коробки.

    Зажмите ctrl и кликните на AuthenticationForm (класс-родитель).

    Вы увидите там поля username и password.
    У нас же вместо поля по ТЗ должно быть login.

    Изменение add_prefix - это недокументирванная возможность.

    Префикс при этом все равно остается пустым (мы его не меняли - значит, пустой).
    А имя поля мы подменяем. И подменяем его только на форме.

    Мы воспользуемся недокументированной возможностью -
    углубляемся в код и самостоятельно смотрим, что
    мы можем унаследовать.

    Зажимаем еще раз ctrl и кликаем до дедушки
    данного класса - до forms.Form.

    Смотрим, что там есть метод add_prefix.
    Читаем, что он делает. Да, мы используем метод не по назначению.
    Потому что он вообще-то префикс должен добавлять, а мы
    подменяем имя поля. Но метод работает. И даже для реального проекта бы подошло.

    Альтернатива этому способу - самописная форма с полем login.
    Затем обработка поля - чтобы данные дошли до адресата.
    Пыолучается сложнее.
    """

    def add_prefix(self, field_name):
        # Если поле в FIELD_NAME_MAPPING, подменить - взять из FIELD_NAME_MAPPING.

        # https://docs.python.org/3.12/library/stdtypes.html#dict.get
        # Обратите внимание: здесь field_name, field_name. Второе упоминание field_name -
        # это значение по умолчанию.
        field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
        return super().add_prefix(field_name)


class SignUpFormRegistrationForm(forms.Form):
    """
    Форма будет проверяться на стороне клиента.
    На стороне сервера - не будет для экономии времени
    в учебной задаче. В реальном проекте на стороне сервера
    проверка обязательна.

    Форму делайте сразу так, как здесь (т.е. наследуясь от Form). Для интересующихся:
    можно было бы сделать ModelForm на основе модели CustomUser.
    Но это очень проблемный вариант.

    Вы можете попробовать раскомментировать
    код такой формы ниже. Это незавершенная форма. Потому что это тупиковое
    направление: нам нужен аттрибут pattern, нужно еще сообщить пользователю
    о требованиях к каждому полю. Это все придется дописывать. В результате

    Еще надо будет добавить повтор пароля, потому что его по умолчанию не будет.

    Выйдет строк кода не меньше, чем написать форму самостоятельно.
    А код, вероятно, станет сложнее.

    Если будете пробовать, раскомментируйте две строки в FIELD_NAME_MAPPING
    из файла accounts/const.py.
    """

    # https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#django.forms.TextInput
    # https://docs.djangoproject.com/en/5.0/ref/forms/fields/#charfield
    # https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#module-django.forms.widgets
    # https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#passwordinput
    # https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#django.forms.Widget.attrs
    # https://docs.djangoproject.com/en/5.0/ref/forms/fields/#label
    # https://docs.djangoproject.com/en/5.0/ref/forms/fields/#emailfield
    # https://docs.djangoproject.com/en/5.0/ref/forms/fields/#booleanfield

    surname = forms.CharField(required=True, widget=forms.TextInput(attrs=ValidationPatterns.VALIDATE_CYR.value, ),
                              label="Фамилия ({})".format(SignUpErrorMessages.CYR_MESSAGE.value))
    name = forms.CharField(required=True, widget=forms.TextInput(attrs=ValidationPatterns.VALIDATE_CYR.value, ),
                           label="Имя ({})".format(SignUpErrorMessages.CYR_MESSAGE.value))
    partonymic = forms.CharField(required=True, widget=forms.TextInput(attrs=ValidationPatterns.VALIDATE_CYR.value, ),
                                 label="Отчество ({})".format(SignUpErrorMessages.CYR_MESSAGE.value))
    login = forms.CharField(required=True, widget=forms.TextInput(attrs=ValidationPatterns.VALIDATE_LAT.value, ),
                            label="Логин ({})".format(SignUpErrorMessages.LAT_MESSAGE.value))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs=ValidationPatterns.VALIDATE_GTE6.value, ),
                               label="Пароль ({})".format(SignUpErrorMessages.GTE6_MESSAGE.value))
    repeated_password = forms.CharField(widget=forms.PasswordInput(attrs=ValidationPatterns.VALIDATE_GTE6.value, ),
                                        label="Повтор пароля")
    email = forms.EmailField(required=True, label="Электронная почта")
    rules = forms.BooleanField(required=True, label="Согласен с правилами регистрации")


# class SignUpFormRegistrationForm(ModelForm):
#     class Meta:
#         model = CustomUser
#         exclude = ["last_login",
#                    "groups",
#                    "user_permissions",
#                    "is_staff",
#                    "is_superuser",
#                    "is_active",
#                    "date_joined",
#                    ]
#
#     def add_prefix(self, field_name):
#         # Если поле в FIELD_NAME_MAPPING, подменить - взять из FIELD_NAME_MAPPING.
#
#         # https://docs.python.org/3.12/library/stdtypes.html#dict.get
#         # Обратите внимание: здесь field_name, field_name. Второе упоминание field_name -
#         # это значение по умолчанию.
#         field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
#         return super().add_prefix(field_name)