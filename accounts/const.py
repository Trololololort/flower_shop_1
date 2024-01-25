from enum import Enum


class SignUpErrorMessages(Enum):
    CYR_MESSAGE = "Допустимы кириллица, пробел и тире."
    LAT_MESSAGE = "Допустимы латиница, цифры и тире."
    GTE6_MESSAGE = "Не менее 6 символов."


class ValidationPatterns(Enum):
    VALIDATE_CYR = {"pattern": "^[А-Яа-яЁё\\- ]+$",
                    "required": True,
                    "title": SignUpErrorMessages.CYR_MESSAGE.value, }
    VALIDATE_LAT = {"pattern": "^[A-Za-z0-9\\-]*$",
                    "required": True,
                    "title": SignUpErrorMessages.LAT_MESSAGE.value, }
    VALIDATE_GTE6 = {"pattern": "^(.{6})(.*)$",
                     "required": True,
                     "title": SignUpErrorMessages.GTE6_MESSAGE.value, }


# Вспомогательный словарь для LoginForm.
FIELD_NAME_MAPPING = {
    'username': 'login',

    # Ниже закомментированы два поля.
    # Это для желающих поэкспериментировать
    # с SignUpFormRegistrationForm(ModelForm).
    # См. комментарий к SignUpFormRegistrationForm(forms.Form) в
    # accounts/forms.py.

    # 'last_name': 'surname',
    # 'first_name': 'name',
}


class HttpStatusCodes(Enum):
    OK = 204
    CONFLICT = 409
