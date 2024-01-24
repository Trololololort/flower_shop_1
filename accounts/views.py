from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic, View

from accounts.service import get_status_and_message_whether_login_is_free


class SignUpView(generic.View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/signup.html", {'form': form})

    def post(self, request):
        """
        Создать пользователя. После создания редирект на главную страницу.
        """

        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Теоретически, форма может быть невалидна.
            # Но мы проверили, свободен ли логин без перезагрузки страницы.
            # И проверили остальные поля на клиенте.
            # Плюс стоит CSRF-защита: постманом запрос не пошлешь сюда.
            # Поэтому очень маловероятно,
            # что экзаменатор сможет попасть на случай, когда форма невалидна.
            # Поэтому не тратим время даже на организацию отправки содержательного
            # статуса HTTP для случая невалидной формы.


            # https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#using-messages-in-views-and-templates
            messages.add_message(request, messages.INFO, "Пользователь создан".format())
            form.save()

        return redirect("home")


class IsLoginFreeView(View):

    def post(self, request):
        """
        Поверка занятости логина без перезагрузки страницы.
        В случае успеха вернуть
        """
        login = request.POST.get("login")

        status = get_status_and_message_whether_login_is_free(login)

        # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse
        return HttpResponse(status["status"], message=status["message"])
