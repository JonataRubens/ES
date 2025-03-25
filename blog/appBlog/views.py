from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


def ListaPosts(request):
    posts = Post.objects.order_by('-data_publicacao')[:10]
    return render(request, 'ListaPosts.html', {'posts': posts})


def Link(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'Post.html',{'post':post})
