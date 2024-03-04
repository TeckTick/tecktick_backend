from django.urls import path
from . import views

urlpatterns = [
    # Blog routes
    path('posts/', views.BlogList.as_view()),
    path('posts/<int:pk>/', views.ListBlogById.as_view()),

    # Comment routes
    path('posts/<int:pk>/comments/', views.CommentList.as_view()),
    path('posts/<int:pk>/comments/<int:comment_id>/', views.ListCommentById.as_view()),
] 