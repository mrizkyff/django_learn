from django.shortcuts import render

def index(request):
    context = {
        'Judul':'Home Page',
        'Content':'Ini adalah homepage dari website ini!',
    }
    return render(request, 'index.html', context)