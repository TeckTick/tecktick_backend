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
    
    # path('partners/', views.partner_list),
    # path('partners/<int:pk>/', views.partners_by_id),

    # # team routes
    # path('team/', views.team_list),
    # path('team/<int:pk>/', views.team_by_id),

    # # testimonial routes
    # path('testimonials/', views.testimonial_list),
    # path('testimonials/<int:pk>/', views.testimonial_by_id),
] 