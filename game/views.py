from django.shortcuts import render, redirect
from users.models import User

# Create your views here.
<<<<<<< HEAD
def gameInfo1(request):
    return render(request, 'gameInfo/gameInfo1.html')

def gameInfo2(request):
    return render(request, 'gameInfo/gameInfo2.html')

def gameInfo3(request):
    return render(request, 'gameInfo/gameInfo3.html')
=======
def create_game(request):
    return render(request, 'smk_gameStart/smk_Attack.html')

def game_list(request):
    return render(request, 'game/cms.html')

# def rank(request):
#     users = User.objects.order_by('-score')[:3]
#     context = {
#         'users':users,
#     }
#     return render(request, 'game/rank.html', context)
>>>>>>> f1d2a0bc48523e989157dfa638fc4a9a7cc0d74a
