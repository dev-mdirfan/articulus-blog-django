from django.shortcuts import render
from blog.models import Post
from blog.views import blog

def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            # context = {
            #     'posts': Post.objects.all()
            # }
            # return render(request, 'blog/blog.html', context)
            # How to run another app's view from here?
            return blog(request)
        else:
            return render(request, 'landing/pages/index.html')
    return render(request, 'landing/pages/index.html')