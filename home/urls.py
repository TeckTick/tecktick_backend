from django.urls import path
from . import views

urlpatterns = [
    # partner routes
    path('partners/', views.PartnerList.as_view()),
    path('partners/<int:pk>/', views.ListPartnersById.as_view()),

#   # team routes
    path('team/', views.TeamList.as_view()),
    path('team/<int:pk>/', views.ListTeamById.as_view()),

    # testimonial routes
    path('testimonials/', views.TestimonialList.as_view()),
    path('testimonials/<int:pk>/', views.ListTestimonialsById.as_view()),
] 