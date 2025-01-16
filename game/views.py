from django.shortcuts import render, redirect
from users.models import CustomUser

# Create your views here.
def gameInfo1(request):
    return render(request, 'gameInfo/gameInfo1.html')

def gameInfo2(request):
    return render(request, 'gameInfo/gameInfo2.html')

def gameInfo3(request):
    return render(request, 'gameInfo/gameInfo3.html')

def create_game(request):
    return render(request, 'smk_gameStart/smk_Attack.html')

def game_list(request, pk):
    user = CustomUser.objects.get(id=pk)
    context = {
        'user': user,
        
    }
    return render(request, 'game/cms.html', context)

def rankings(request):
    users = CustomUser.objects.order_by('-score')[:3]
    context = {
        'users':users,
    }
    return render(request, 'game/rank.html', context)

def smk_Attack(request):
    return render(request, 'smk_gameStart/smk_Attack.html')
def smk_CounterAttack(request):
    return render(request, 'smk_gameStart/smk_CounterAttack.html')