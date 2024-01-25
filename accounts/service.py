from django.contrib.auth.models import User

from accounts.const import HttpStatusCodes
from accounts.models import CustomUser


def get_status_and_message_whether_login_is_free(login):
    """
    В зависимости от того, занят ли логин,
    подготовить коды ответа на запрос к серверу.

    Ответ: 1) 204 -  логин свободен.
           2) 409 - логин занят.
    """
    status = {"status": HttpStatusCodes.OK.value, "message": "Login is free"}

    # https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-specific-objects-with-filters
    occupied_login = bool(User.objects.filter(username=login).first())

    if occupied_login:
        status = {"status": HttpStatusCodes.CONFLICT.value, "message": "Login is occupied"}

    return status


def create_user(surname,
                name,
                partonymic,
                login,
                email,
                rules,
                password):
    user = CustomUser.objects.create(last_name=surname,
                                     first_name=name,
                                     partonymic=partonymic,
                                     username=login,
                                     password=password,
                                     email=email,
                                     rules=rules)

    # Когда передали пароль в метод create,
    # для нас это была, по сути, заглушка.
    # Дело в том, что он сохранится в неизменном виде.
    # А вся система аутентификации Django ориентируется
    # На хеширование паролей. Иначе говоря,
    # если оставить, как было, пользователь не сможет логиниться.
    # Сохраним хэшированный пароль.
    user.set_password(user.password)

    user.save()
