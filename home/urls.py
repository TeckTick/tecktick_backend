from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'partners', views.PartnerViewSet, basename='partner')
router.register(r'testimonials', views.TestimonialViewSet, basename='testimonial')
router.register(r'teams', views.TeamViewSet, basename='team')

urlpatterns = router.urls

# urlpatterns = [
#     # partner routes
#     path('partners/', views.PartnerList.as_view()),
#     path('partners/<int:pk>/', views.ListPartnersById.as_view()),

# #   # team routes
#     path('team/', views.TeamList.as_view()),
#     path('team/<int:pk>/', views.ListTeamById.as_view()),

#     # testimonial routes
#     path('testimonials/', views.TestimonialList.as_view()),
#     path('testimonials/<int:pk>/', views.ListTestimonialsById.as_view()),
    
# ] 
