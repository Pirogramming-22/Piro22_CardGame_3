from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User  # 기본 User 모델 사용
from django.contrib import messages

def main(request):
    return render(request, "auth/main.html")

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # 비밀번호 확인
        if password1 == password2:
            # 사용자 생성
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                )
                auth.login(request, user)
                return redirect('users:main')
            except Exception as e:
                messages.error(request, f"Error creating account: {e}")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'auth/signup.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('users:main')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('users:main')
