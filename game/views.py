from django.shortcuts import render

# Create your views here.
def gameInfo(request):
    return render(request, 'gameInfo/gameInfo1.html')