from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'posts/index.html')


def all(request):
    return render(request, 'posts/index.html')


def detail(request):
    return render(request, 'posts/detail.html')


def star(request):
    return render(request, 'posts/star.html')


def mypage(request):
    return render(request, 'posts/mypage.html')


def lists(request):
    return render(request, 'posts/lists.html')


def scroll(request):
    return render(request, 'posts/scroll.html')



