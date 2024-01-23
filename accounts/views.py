from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic





class SignUpView(generic.View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/signup.html", {'form': form})


    def post(self, request):
        """
        Создать пользователя. После создания редирект на главную страницу.
        """

        form = UserCreationForm(request .POST)
        if form.is_valid():
            form.save()

        return redirect("home")
