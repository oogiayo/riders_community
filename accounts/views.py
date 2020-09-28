from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
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


@require_http_methods(['GET', 'POST'])
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


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method=='POST':
        update_form = CustomUserChangeForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('posts:index')
    # user = request.user
    else:
            update_form = CustomUserChangeForm(instance=request.user)
    context = {
        'update_form': update_form,
    }
    return render(request, 'accounts/update.html', context)


@require_http_methods(['GET', 'POST'])
def delete(request):
    if request.user.is_authenticated:
        if request.method=='POST':       
            request.user.delete()
            return redirect('posts:index')
        return render(request, 'accounts/delete.html')
    # 비회원 접근 시 로그인페이지로 이동
    return redirect('accounts:login')


@require_http_methods(['GET', 'POST'])
def password_change(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            pw_form = PasswordChangeForm(request.user, request.POST)
            if pw_form.is_valid():
                pw_form.save()
                auth_login(request, request.user)
                return redirect('posts:index')
        else:
            pw_form = PasswordChangeForm(request.user)
        context = {
            'pw_form': pw_form,
        }
        return render(request, 'accounts/password_change.html', context)
    # 비회원 접근 시 로그인페이지로 이동
    return redirect('accounts:login')
