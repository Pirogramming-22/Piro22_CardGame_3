from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser
import random
from .models import Game
from django.db.models import Q
# Create your views here.
def gameInfo1(request, game_id):
    game = get_object_or_404(Game, id=game_id)  # game_id로 게임 객체를 가져옴
    return render(request, 'gameInfo/gameInfo1.html', {'game': game})

def gameInfo2(request, game_id):
    game = get_object_or_404(Game, id=game_id)  # game_id로 게임 객체를 가져옴
    return render(request, 'gameInfo/gameInfo2.html', {'game': game})

def gameInfo3(request, game_id):
    game = get_object_or_404(Game, id=game_id)  # game_id로 게임 객체를 가져옴
    return render(request, 'gameInfo/gameInfo3.html', {'game': game})


def create_game(request):
    defenders = CustomUser.objects.exclude(id=request.user.id)
    random_numbers = random.sample(range(1, 11), 5)  # 랜덤 숫자 생성

    return render(request, 'smk_gameStart/smk_Attack.html', {
        'defenders': defenders,
        'random_numbers': random_numbers,
    })

def attackSave(request):
    if request.method == 'POST':
        defender_id = request.POST.get('defender')
        defender = CustomUser.objects.get(id=defender_id)
        attacker = request.user
        selected_card = request.POST.get('card')
        is_greater_wins = random.choice([True, False])
        
        
        if defender and attacker and selected_card:
            new_game = Game(attacker=attacker, defender=defender, attacker_card=selected_card, is_greater_wins=is_greater_wins)
            game = new_game.save()
            return redirect('game:game_list', attacker.id)

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

def cancel_game(request, game_id):
    game = Game.objects.get(id=game_id)
    if game.attacker.username == request.user.username:
        game.delete()
    return redirect('game:game_list', request.user.id)

def respondSave(request, game_id):
    if request.method == 'POST':
        game = Game.objects.get(id=game_id)
        if game.defender == request.user:
            game.defender_card = int(request.POST.get('card'))
            game.save()
            attacker = CustomUser.objects.get(id=game.attacker.id)
            defender = CustomUser.objects.get(id=game.defender.id)
            result = game_result(game.attacker_card, game.defender_card, game.is_greater_wins)
            score = abs(game.attacker_card - game.defender_card)
            if result == 0:
                game.winner = None
            elif result == 1:
                game.winner = attacker
                attacker.score += score
                defender.score -= score
            else:
                game.winner = defender
                defender.score += score
                attacker.score -= score
            attacker.save()
            defender.save()
            game.save()
            return redirect('game:game_list', defender.id)
            

def game_result(user1_card, user2_card, is_greater_wins):
    if user1_card == user2_card:
        return 0 #무승부
    if is_greater_wins:
        return 1 if user1_card > user2_card else 2 #1: user1 승, 2: user2 승
    return 1 if user1_card < user2_card else 2
            