from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'posts/index.html')


def search(request):
    return render(request, 'posts/search.html')