from django.db import models
from mdeditor.fields import MDTextField  # 使用富文本字段
from django.db.models import Count

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self): return self.name

class Article(models.Model):
    title = models.CharField("标题", max_length=200)
    cover = models.ImageField("封面图", upload_to='covers/', blank=True, null=True)
    # 使用 MDTextField 替换普通 TextField，后台会出现 Markdown 编辑器
    content = MDTextField("正文") 
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="标签")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章管理"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    # --- 核心：极简推荐算法 ---
    def get_recommendations(self):
        # 1. 获取当前文章所有标签的 ID
        article_tags_ids = self.tags.values_list('id', flat=True)
        # 2. 找包含这些标签的其他文章，排除自己
        return Article.objects.filter(tags__in=article_tags_ids)\
                              .exclude(id=self.id)\
                              .annotate(same_tags=Count('tags'))\
                              .order_by('-same_tags', '-created_at')[:5]

class Project(models.Model):
    name = models.CharField("项目名称", max_length=100)
    desc = models.TextField("简介")
    url = models.URLField("项目地址")
    image = models.ImageField("展示图", upload_to='projects/')
    
    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目集"

    def __str__(self):
        return self.name
