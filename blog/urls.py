from django.urls import path
from . import views

urlpatterns = [
    # Blog routes
    path('post/', views.BlogList.as_view()),
    path('blog/<int:pk>/', views.ListBlogById.as_view()),
] 