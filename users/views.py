from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from users.forms import *


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
    user = UserCreationForm(request.POST)
    user_from = UserForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if request.method == 'POST':
        if user.is_valid() and user_from.is_valid() and profile_form.is_valid():
            user.save()
            user_from.save()
            return redirect('login')
    user = UserCreationForm()
    user_from = UserForm()
    profile_form = ProfileForm()
    return render(request, 'reg.html', {'user': user, 'user_form': user_from, 'profile_form': profile_form})


class LogoutFormView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
        pass
