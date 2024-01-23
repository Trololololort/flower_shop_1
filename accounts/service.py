from django.contrib.auth.models import User


def is_login_occupied(login):
    """
    Организация проверки логина без перезагрузки страницы.
    В зависимости от того, занят ли логин,
    отправить 204 или 409.
    """
    status = {"status": 204, "message": "Login is free"}

    occupied_login = User.objects.filter(username=login).first()

    if occupied_login:
        status = {"status": 409, "message": "Login is occupied"}

    return status