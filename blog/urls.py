from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('articles/', views.articles, name='articles'),
    path('about/', views.about, name='about'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
]
