from django.shortcuts import render

# Create your views here.
def create_game(request):
    return render(request, 'smk_gameStart/smk_Attack.html')

def game_list(request):
    return render(request, 'game/cms.html')

def rankings(request):
    return render(request, 'game/jwj.html')