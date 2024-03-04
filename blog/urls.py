from django.urls import path
from . import views

urlpatterns = [
    # blog routes
    # path('articles', views.BlogList.as_view()),
    # path('articles/<int:pk>/', views.ListBlogById.as_view()),



    # comment routes
    path('articles/<int:pk>/comments/', views.CommentList.as_view()),
   
] 