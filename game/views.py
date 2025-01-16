from django.shortcuts import render, redirect
from users.models import User

# Create your views here.
def rank(request):
    users = User.objects.order_by('-score')[:3]
    context = {
        'users':users,
    }
    return render(request, 'game/rank.html', context)