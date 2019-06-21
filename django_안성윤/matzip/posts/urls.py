from django.urls import path, include
from . import views

app_name = 'posts'


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('star/', views.star, name='star'),
    path('mypage/', views.mypage, name='mypage'),

]

