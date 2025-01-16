from django.shortcuts import render

# Create your views here.
def gameInfo1(request):
    return render(request, 'gameInfo/gameInfo1.html')

def gameInfo2(request):
    return render(request, 'gameInfo/gameInfo2.html')

def gameInfo3(request):
    return render(request, 'gameInfo/gameInfo3.html')