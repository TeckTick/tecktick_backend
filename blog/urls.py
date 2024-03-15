from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CommentViewSet, ReplyViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'replies', ReplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
