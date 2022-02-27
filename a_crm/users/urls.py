from django.urls import path
from users.views import RegisterView, AuthView
urlpatterns = [
    path("registration/",RegisterView.as_view(), name="regist_view"),
    path("authorization/",AuthView.as_view(), name="auth_view"),
]
