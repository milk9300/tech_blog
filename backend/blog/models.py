from django.db import models
from django.utils.text import slugify
from pypinyin import pinyin, Style

def generate_pinyin_slug(text):
    """
    Converts Chinese text to pinyin slugs.
    Example: "后端设计" -> "hou-duan-she-ji"
    """
    pinyin_list = pinyin(text, style=Style.NORMAL)
    flat_pinyin = '-'.join([item[0] for item in pinyin_list])
    return slugify(flat_pinyin)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="分类名称")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="URL标识")
    description = models.TextField(blank=True, verbose_name="描述")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_pinyin_slug(self.name)
        super().save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="标签名称")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="URL标识")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_pinyin_slug(self.name)
        super().save(*args, **kwargs)

class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', '草稿'),
        ('published', '已发布'),
    )

    title = models.CharField(max_length=200, verbose_name="标题")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="URL标识")
    summary = models.TextField(verbose_name="摘要")
    content = models.TextField(verbose_name="正文")
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name="封面图")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="状态")
    view_count = models.PositiveIntegerField(default=0, verbose_name="浏览次数")
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles', verbose_name="分类")
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles', verbose_name="标签")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="发布时间")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_pinyin_slug(self.title)
        super().save(*args, **kwargs)

class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="电子邮箱")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="订阅时间")
    is_active = models.BooleanField(default=True, verbose_name="是否激活")

    class Meta:
        verbose_name = "订阅者"
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def __str__(self):
        return self.email
