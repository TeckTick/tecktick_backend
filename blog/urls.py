from django.urls import path
from . import views

urlpatterns = [
    # blog routes
    # path('blogs/', views.BlogList.as_view()),
    # path('blogs/<int:pk>/', views.ListBlogById.as_view()),



    # comment routes
    path('comments/', views.CommentList.as_view()),
   
] 