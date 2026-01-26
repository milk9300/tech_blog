from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet, ArticleViewSet, SubscriberViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'subscribers', SubscriberViewSet)

urlpatterns = router.urls
