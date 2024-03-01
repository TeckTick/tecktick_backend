from django.urls import path
from . import views

urlpatterns = [
    # team routes
    path('team/', views.TeamList.as_view()),
    path('team/<int:pk>/', views.ListTeamById.as_view()),

] 