from django.contrib import admin
from django.utils import timezone
from .models import Category, Tag, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # --- 列表页配置 ---
    list_display = ('title', 'status', 'category', 'view_count', 'published_at', 'updated_at')
    list_filter = ('status', 'category', 'tags')
    search_fields = ('title', 'content', 'summary')
    # date_hierarchy = 'created_at'
    list_editable = ('status',)  # 允许在列表页快速切换状态
    ordering = ('-updated_at',)

    # --- 表单字段分组 ---
    fieldsets = (
        ('基础信息', {
            'fields': ('title', 'slug', 'status'),
            'classes': ('wide',),
        }),
        ('内容区域', {
            'fields': ('summary', 'content'),
            'classes': ('wide',),
            'description': '摘要用于列表页展示，正文支持 Markdown 格式。'
        }),
        ('分类与标签', {
            'fields': ('category', 'tags'),
            'classes': ('collapse',),  # 默认折叠
        }),
        ('媒体', {
            'fields': ('cover_image',),
            'classes': ('collapse',),
        }),
        ('时间与统计', {
            'fields': ('published_at', 'view_count', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    # --- 只读字段 ---
    readonly_fields = ('view_count', 'created_at', 'updated_at')

    # --- Slug 自动填充 ---
    prepopulated_fields = {'slug': ('title',)}

    # --- 多对多字段优化 ---
    filter_horizontal = ('tags',)

    # --- 外部资源 (EasyMDE + 自定义样式) ---
    class Media:
        css = {
            'all': (
                'https://cdn.jsdelivr.net/npm/easymde/dist/easymde.min.css',
                'admin/css/article_admin.css',
            )
        }
        js = (
            'https://cdn.jsdelivr.net/npm/easymde/dist/easymde.min.js',
            'admin/js/easymde_init.js',
        )

    # --- 发布流程优化 ---
    def save_model(self, request, obj, form, change):
        """
        发布时自动设置发布时间。
        - status == 'draft': 不设置 published_at
        - status == 'published' 且 published_at 为空: 自动填充当前时间
        """
        if obj.status == 'published' and not obj.published_at:
            obj.published_at = timezone.now()
        super().save_model(request, obj, form, change)
