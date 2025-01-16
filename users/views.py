from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'auth/main.html')

def login_view(request):
  return render(request, 'auth/login.html')

def signup_view(request):
  return render(request, 'auth/signup.html')
  