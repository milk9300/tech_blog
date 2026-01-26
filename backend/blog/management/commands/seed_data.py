from django.core.management.base import BaseCommand
from blog.models import Category, Tag, Article
from django.utils import timezone
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Categories
        cat_python, _ = Category.objects.get_or_create(
            name='Python', 
            defaults={'slug': 'python', 'description': 'Python 编程相关'}
        )
        cat_web, _ = Category.objects.get_or_create(
            name='Web开发', 
            defaults={'slug': 'web-development', 'description': '前端与后端开发技术'}
        )

        # Tags
        tag_django, _ = Tag.objects.get_or_create(name='Django', defaults={'slug': 'django'})
        tag_vue, _ = Tag.objects.get_or_create(name='Vue', defaults={'slug': 'vue'})
        tag_drf, _ = Tag.objects.get_or_create(name='DRF', defaults={'slug': 'drf'})
        tag_docker, _ = Tag.objects.get_or_create(name='Docker', defaults={'slug': 'docker'})

        # Articles
        # Article 1
        a1, created = Article.objects.get_or_create(
            slug='hello-world',
            defaults={
                'title': 'Hello World: 我的第一篇博客',
                'summary': '这是基于 Django 和 Vue 构建的个人博客系统的第一篇文章。',
                'content': '''# Hello World

欢迎来到我的技术博客！

这是系统的第一篇文章，用于验证功能是否正常。

## 技术栈

* **Backend**: Django 5 + DRF
* **Frontend**: Vue 2
* **Database**: MySQL (Local: SQLite)

```python
def hello():
    print("Hello World")
```
''',
                'status': 'published',
                'category': cat_web,
                'published_at': timezone.now()
            }
        )
        if created:
            a1.tags.add(tag_django, tag_vue)
            a1.save()

        # Article 2
        a2, created = Article.objects.get_or_create(
            slug='django-drf-tutorial',
            defaults={
                'title': 'Django DRF 快速入门',
                'summary': 'Django Rest Framework 是构建 Web API 的强大工具。',
                'content': '''# Django DRF

DRF 提供了序列化器、视图集等强大的组件。

## 安装

```bash
pip install djangorestframework
```

## 配置

在 `settings.py` 中添加:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
''',
                'status': 'published',
                'category': cat_python,
                'published_at': timezone.now()
            }
        )
        if created:
            a2.tags.add(tag_django, tag_drf)
            a2.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded data'))
