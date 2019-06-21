from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    user = request.user

    posts = Post.objects.filter(user__in=user.follow.all())
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form
    }
    return render(request, 'posts/index.html', context)


def all(request):
    posts = Post.objects.all().order_by('-id')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form
    }
    return render(request, 'posts/index.html', context)


def detail(request):
    return render(request, 'posts/detail.html')


def star(request):
    return render(request, 'posts/star.html')