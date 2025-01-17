from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser
import random
from .models import Game
from django.db.models import Q
# Create your views here.
def gameInfo1(request):
    return render(request, 'gameInfo/gameInfo1.html')

def gameInfo2(request):
    return render(request, 'gameInfo/gameInfo2.html')

def gameInfo3(request):
    return render(request, 'gameInfo/gameInfo3.html')

def create_game(request):
    defenders = CustomUser.objects.exclude(id=request.user.id)
    random_numbers = random.sample(range(1, 11), 5)  # 랜덤 숫자 생성

    return render(request, 'smk_gameStart/smk_Attack.html', {
        'defenders': defenders,
        'random_numbers': random_numbers,
    })

def game_list(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    games = Game.objects.filter(Q(attacker=user) | Q(defender=user))
    context = {
        'user': user,
        'games': games,
    }
    return render(request, 'game/cms.html', context)

def rankings(request):
    users = CustomUser.objects.order_by('-score')[:3]
    context = {
        'users':users,
    }
    return render(request, 'game/rank.html', context)

def respond_game(request, game_id):
    game = get_object_or_404(Game, id=game_id) # 1. game_id로 특정 게임 객체 가져오기
    random_numbers = random.sample(range(1, 11), 5) # 2. 랜덤 숫자 생성 (1~10 중 5개)
    return render(request, 'smk_gameStart/smk_CounterAttack.html', {  # 3. 템플릿에 데이터 전달
        'game': game,  # 게임 객체
        'random_numbers': random_numbers,  # 랜덤 숫자
    })
