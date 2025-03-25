from django.shortcuts import render
from .models import Post

def lista_posts(request):
    posts = Post.objects.order_by('-data_publicacao')[:10]
    return render(request, 'lista_posts.html', {'posts': posts})


def test_link(request, id):
    post = get_object_or_404(Post,id=id)
    return render (request,'Post.html',{'Post':post})