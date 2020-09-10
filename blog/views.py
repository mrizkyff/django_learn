from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    posts = Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context = {
        'Judul':'Home Blog',
        'Content':'Ini adalah halaman blog!',
        'Posts':posts,
        'Categories':categories,
    }

    return render(request, 'blog/index.html', context)

def detailPost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)
    context = {
        'Judul':'Home Blog',
        'Content':'Ini adalah halaman blog!',
        'DetailPost':posts,
    }

    return render(request, 'blog/detail.html', context)

def categoryPost(request, categoryInput):
    posts = Post.objects.filter(category=categoryInput)

    categories = Post.objects.values('category').distinct()

    context = {
        'Judul':'Home Blog',
        'Content':'Tampilkan berdasarkan category',
        'Posts':posts,
        'Categories':categories,
    }

    return render(request, 'blog/category.html', context)
