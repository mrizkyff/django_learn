from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'Judul':'Home Blog',
        'Content':'Ini adalah halaman blog!',
    }

    return render(request, 'blog/index.html', context)