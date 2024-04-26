from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
# AuthenticationForm() - 로그인 인증에 사용할 데이터를 입력 받는 built-in form
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import PasswordChangeForm
# login_required - 로그인상태가 아니면 로그인 페이지로 redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

# 로그인 기능
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # get_user() - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환
            auth_login(request, form.get_user()) 
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃 기능
@login_required 
def logout(request):
    auth_logout(request)
    return redirect('movies:index')

# 회원정보가입 기능
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

# 정보수정 기능
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

# 비밀번호변경 기능
@login_required
def password_update(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = PasswordChangeForm(user)
    context = {
        'form': form
    }
    return render(request, 'accounts/password_update.html', context)

# 삭제 기능
@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')