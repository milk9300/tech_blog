from django.shortcuts import render, get_object_or_404
from .models import Article, Project
import markdown

def index(request):
    """首页：精选内容展示"""
    featured_projects = Project.objects.all()[:3]
    featured_articles = Article.objects.all()[:3]
    return render(request, 'index.html', {
        'featured_projects': featured_projects, 
        'featured_articles': featured_articles
    })

def projects(request):
    """项目列表页"""
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def articles(request):
    """文章列表页"""
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def about(request):
    """关于我页面"""
    return render(request, 'about.html')

def article_detail(request, pk):
    """文章详情页"""
    article = get_object_or_404(Article, pk=pk)
    
    # 渲染 Markdown (支持代码高亮)
    article.html_content = markdown.markdown(
        article.content,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite', # 代码高亮
            'markdown.extensions.toc',        # 目录
        ]
    )
    
    # 获取推荐
    recommendations = article.get_recommendations()
    
    return render(request, 'detail.html', {
        'article': article, 
        'recommendations': recommendations
    })
