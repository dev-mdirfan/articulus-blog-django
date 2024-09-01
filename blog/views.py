from django.shortcuts import render
from .models import Post
# Import User
from django.contrib.auth.models import User

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    # print(str(Post.author))
    return render(request, 'blog/blog.html', context)


def blog2(request):
    return render(request, 'blog/blog2.html')

def articulars(request):
    articulars = User.objects.all()
    # print([user for user in articulars])
    context = {
        'articulars': articulars
    }
    return render(request, 'blog/articulars.html', context)