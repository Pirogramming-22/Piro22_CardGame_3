from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from users.forms import SignupForm
from django.contrib import messages
from django.urls import reverse

# 메인 페이지 렌더링
def main(request):
    return render(request, "auth/main.html")

# 회원가입 뷰
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "회원가입이 완료되었습니다.")
            return redirect(reverse('users:main'))
        else:
            messages.error(request, "회원가입에 실패했습니다. 입력 정보를 확인하세요.")
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})

# 로그인 뷰
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)  # 로그인 처리
            messages.success(request, f"환영합니다, {user.username}님!")
            return redirect(reverse('users:main'))
        else:
            messages.error(request, "로그인에 실패했습니다. 아이디와 비밀번호를 확인하세요.")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

# 로그아웃 뷰
def logout(request):
    auth.logout(request)  # 로그아웃 처리
    messages.info(request, "성공적으로 로그아웃되었습니다.")
    return redirect(reverse('users:main'))
