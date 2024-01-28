from django.contrib.auth.hashers import make_password

from accounts.const import HttpStatusCodes
from accounts.models import CustomUser


def get_status_and_message_whether_login_is_free(login):
    """
    В зависимости от того, занят ли логин,
    подготовить коды ответа на запрос к серверу.

    Ответ: 1) 200 -  логин свободен.
           2) 409 - логин занят.
    """

    # https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-specific-objects-with-filters
    login_is_occupied = bool(CustomUser.objects.filter(username=login).first())

    if not login_is_occupied:
        status_code = HttpStatusCodes.OK.value
    else:
        status_code = HttpStatusCodes.CONFLICT.value

    return status_code

    # Если в метод create передать пароль, как есть,
    # он сохранится в открытом виде.
    # А вся система аутентификации Django ориентируется
    # на хеширование паролей. Иначе говоря,
    # если оставить, как было, пользователь не сможет логиниться.
    # Поэтому сохраним хэшированный пароль,
    # воспользовавшись готовой функцией make_password.

def create_user(surname,
                name,
                patronymic,
                login,
                email,
                rules,
                password):
    user = CustomUser.objects.create(last_name=surname,
                                     first_name=name,
                                     patronymic_name=patronymic,
                                     username=login,
                                     password=make_password(password), # Функция из модуля django.contrib.auth.hashers
                                     email=email,
                                     rules=rules)




    user.save()
