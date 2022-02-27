from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from users.models import User

from django.views.generic.base import View
from django.contrib.auth import logout
from users.forms import RegisterForm, LoginForm

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "regist.html"
    success_url = "/klients/page"
    
    def form_valid(self, form):
        form.save()
        redirect('/users/')
        return super(RegisterView, self).form_valid(form)


class AuthView(FormView):
    form_class = LoginForm
    template_name = "author.html"
    success_url = "/klients/page"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(AuthView, self).form_valid(form)

class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/")


