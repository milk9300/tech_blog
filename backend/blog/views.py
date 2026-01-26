from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Tag, Article, Subscriber
from .serializers import CategorySerializer, TagSerializer, ArticleListSerializer, ArticleDetailSerializer, SubscriberSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Article.objects.filter(status='published').order_by('-published_at')
        category = self.request.query_params.get('category')
        tag = self.request.query_params.get('tags')
        search = self.request.query_params.get('search')

        if category:
            queryset = queryset.filter(category__slug=category)
        if tag:
            queryset = queryset.filter(tags__slug=tag)
        if search:
            from django.db.models import Q
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(summary__icontains=search) | 
                Q(content__icontains=search)
            )
        
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer
    
    @action(detail=False, methods=['get'])
    def popular(self, request):
        queryset = self.get_queryset().order_by('-view_count')[:5]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save(update_fields=['view_count'])
        return super().retrieve(request, *args, **kwargs)

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get_permissions(self):
        if self.action in ['create', 'stats']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny])
    def stats(self, request):
        count = Subscriber.objects.filter(is_active=True).count()
        return Response({'count': count})
