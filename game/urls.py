from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('create/', views.create_game, name='create_game'),  # 게임 생성 (공격)
    path('attackSave/', views.attackSave, name='attackSave'),  # 게임 생성 (공격)
    # path('<int:game_id>/', views.game_detail, name='game_detail'),  # 특정 게임 상세 보기
    path('list/<int:user_id>/', views.game_list, name='game_list'),  # 게임 리스트 보기
    path('cancel/<int:game_id>/', views.cancel_game, name='cancel_game'),
    path('gameInfo1/<int:game_id>/', views.gameInfo1, name='gameInfo1'), #게임 진행중일때 정보
    path('gameInfo2/<int:game_id>/', views.gameInfo2 ,name='gameInfo2'), # 카운터 어텍 상황일때 정보
    path('gameInfo3/<int:game_id>/', views.gameInfo3, name='gameInfo3'), # 게임 결과가 나왔을때 정보
    path('respond/<int:game_id>/', views.respond_game, name='respond_game'),  # 게임에 반격
    path('respondSave/<int:game_id>', views.respondSave, name='respondSave'),
    path('rankings/', views.rankings, name='rankings'),  # 랭킹 보기
]