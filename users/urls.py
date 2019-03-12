from django.urls import path, re_path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('login', LoginFormView.as_view()),
    path('logout', LogoutFormView.as_view()),
    path('reg', registration),
    re_path(r'^(?P<id>\d+)$', ProfileUser.as_view(), name='profile'),
]

