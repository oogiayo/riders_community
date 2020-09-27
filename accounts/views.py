from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('accounts:login')
    else:
        signup_form = CustomUserCreationForm()
    context = {
        'signup_form': signup_form,
    }    
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('posts:index')
    else:
        login_form =  AuthenticationForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('posts:index')
