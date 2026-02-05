from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from unfold.admin import ModelAdmin  # <--- 引入 Unfold 的基类
from .models import Article, Tag, Project

# 卸载原生 User Admin，换上 Unfold 风格
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ['name', 'url']

@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    filter_horizontal = ['tags'] # 优化多选框
    list_filter = ['created_at', 'tags']
