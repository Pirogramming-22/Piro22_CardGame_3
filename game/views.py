from django.shortcuts import render, redirect
from users.models import User

# Create your views here.
def create_game(request):
    return render(request, 'smk_gameStart/smk_Attack.html')

def game_list(request, pk):
    user = User.objects.get(id=pk)
    context = {
        'user': user,
        
    }
    return render(request, 'game/cms.html', context)

def rankings(request):
    users = User.objects.order_by('-score')[:3]
    context = {
        'users':users,
    }
    return render(request, 'game/rank.html', context)