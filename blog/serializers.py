from rest_framework import serializers
from .models import Category, Tag, Article, Subscriber

class CategorySerializer(serializers.ModelSerializer):
    articles_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'articles_count']

    def get_articles_count(self, obj):
        return obj.articles.filter(status='published').count()

class TagSerializer(serializers.ModelSerializer):
    articles_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'articles_count']

    def get_articles_count(self, obj):
        return obj.articles.filter(status='published').count()

class ArticleListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'summary', 'cover_image', 'status', 'view_count', 'category', 'tags', 'published_at']

class ArticleDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['id', 'email', 'created_at', 'is_active']
        read_only_fields = ['id', 'created_at', 'is_active']
