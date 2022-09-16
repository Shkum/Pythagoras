from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'info': 'TEST PAGE',
    }
    return render(request, 'Pythagoras_matrix/index.html', context=context)
