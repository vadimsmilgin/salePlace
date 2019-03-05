from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from shop.forms import CreationItemForm
from shop.models import Item
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


def registration(request):
    if request.method == 'POST':
        form = SingUp(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            profile = Profile()
            profile.user = user
            profile.ava = request.FILES['account_image']
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


class ProfileUser(DetailView):

    template_name = "profile.html"

    def get(self, request, id):
        form = CreationItemForm()
        user = get_object_or_404(User, id=id)
        profile = get_object_or_404(Profile, user=user)
        items = Item.objects.filter(owner=id)
        #users = User.objects.all().select_related('profile')
        return render(request, self.template_name, {'current_user': user, 'profile': profile, 'form': form, 'items': items})

    def post(self, request, *args, **kwargs):
        form = CreationItemForm(request.POST, request.FILES)
        if form.is_valid():
            id = kwargs['id']
            cd = form.cleaned_data
            user = get_object_or_404(User, id=id)
            profile = get_object_or_404(Profile, user=user)

            item = Item(owner=user,
                        category=cd['category'],
                        icon=cd['icon'],
                        name=cd['name'],
                        price=cd['price'],
                        description=cd['description']).save()
            self.get(request,id)
        form = CreationItemForm()
        return render(request, self.template_name, {'current_user': user, 'profile': profile, 'form': form})