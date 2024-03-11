from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('profile/update/', views.UpdateProfile.as_view(), name='update_profile'),
]
