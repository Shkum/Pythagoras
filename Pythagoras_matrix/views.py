from django.shortcuts import render

from .forms import UserData


def index(request):
    context = {
        'info': 'РАСЧЕТ ПИФАГОРА',

        'range': range(1, 4),

        'form': UserData(request.POST or None),
    }

    if request.method == 'POST':
        print(request.POST)

    return render(request, 'Pythagoras_matrix/index.html', context=context)
