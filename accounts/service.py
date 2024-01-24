from django.contrib.auth.models import User
from enum import Enum


class HttpStatusCodes(Enum):
    OK = 204
    CONFLICT = 409


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
