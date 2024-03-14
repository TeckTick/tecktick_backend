from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'register', views.RegisterViewSet, basename='register')
router.register(r'login', views.LoginViewSet, basename='login')
router.register(r'logout', views.LogoutViewSet, basename='logout')

urlpatterns = [
    path('profile/', views.UpdateProfileViewSet.as_view(), name='profile'),
] + router.urls


# urlpatterns = router.urls
# urlpatterns = [
#     path('register/', views.Register.as_view(), name='register'),
#     path('login/', views.Login.as_view(), name='login'),
#     path('logout/', views.Logout.as_view(), name='logout'),
#     path('profile/', views.Profile.as_view(), name='profile'),
#     path('profile/update/', views.UpdateProfile.as_view(), name='update_profile'),
# ]


