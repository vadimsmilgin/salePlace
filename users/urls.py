from django.urls import path, re_path
from users.views import LoginFormView, LogoutFormView, RegistrationFormView, registrationUser

urlpatterns = [
    path('login', LoginFormView.as_view()),
    path('logout', LogoutFormView.as_view()),
    path('reg', registrationUser),
]