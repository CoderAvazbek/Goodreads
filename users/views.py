from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm
        context = {
            "form": create_form
        }
        return render(request, 'users/register.html', context)
    
    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            messages.success(request, "You have successfully Register")
            return redirect('login')
        else:
            context = {
                "form": create_form
            }
            return render(request, "users/register.html", context)

class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        context = {
            "login_form": login_form
        }
        return render(request, 'users/login.html', context)
    
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect('landing-page')
        else:
            return render(request, 'users/login.html', {"login_form": login_form})


class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        return render(request, 'users/profile.html', {"user": request.user})
    

class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have successfully")
        return redirect('landing-page')