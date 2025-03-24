from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render , get_list_or_404
from .models import Post


def lista_posts(request):
    posts = Post.objects.order_by('-data_publicacao')[:10]
    return render(request, 'lista_posts.html', {'posts': posts})


def post_detail(request, pk):
    post = get_list_or_404(Post, pk=pk)
    
    return render(request, 'blog/lista_posts.html', {'post':post})