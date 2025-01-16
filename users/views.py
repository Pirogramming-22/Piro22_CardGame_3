from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from users.forms import SignupForm

def main(request):
    return render(request, "auth/main.html")


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('users:main')
        else:
            # return redirect('users:signup')
            return render(request, 'auth/signup.html', {'form': form})
    else:
        form = SignupForm()
        context = {
            'form': form,
        }
        return render(request, template_name='auth/signup.html', context=context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('users:main')
        else:
            context = {
                'form':form,
            }
            return render(request, template_name='auth/login.html',context=context)
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, template_name='auth/login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect('users:main')