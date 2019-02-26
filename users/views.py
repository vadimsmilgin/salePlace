from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from users.forms import *
from users.models import Profile


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
        pass


class RegistrationFormView(FormView):
    form_class = UserCreationForm
    template_name = "reg.html"
    success_url = "login"

    def form_valid(self, form):
        form.save()
        return super(RegistrationFormView, self).form_valid(form)
        pass


def registrationUser(request):
    if request.method == 'POST':
        form = SingUp(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            profile = Profile()
            profile.user = user
            profile.ava = form.cleaned_data.get('account_image')
            profile.save()
            return HttpResponseRedirect("/users/login")
    else:
        form = SingUp()
    return render(request, 'reg.html', {'form': form})


class LogoutFormView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
        pass
