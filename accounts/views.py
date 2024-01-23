from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic, View

from accounts.service import is_login_occupied


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
            form.save()

        return redirect("home")


class IsLoginOccupiedView(View):

    def post(self, request):
        """
        Поверка занятости логина без перезагрузки страницы.
        """
        login = request.POST.get("login")

        status = is_login_occupied(login)

        return HttpResponse(status["status"], message=status["message"])
