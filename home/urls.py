from django.urls import path
from . import views

urlpatterns = [
    # path('', home, name='home'),
    path('partners/<int:pk>', views.ListPartnersById.as_view(), name='list-partners-by-id'),
    path('partners/update/<int:pk>/', views.UpdatePartners.as_view(), name='update-partner'),
    path('partners/<int:pk>/delete/', views.DeletePartners.as_view(), name='delete-partner'),
    path('partners/new/', views.PostPartners.as_view(), name='create-partner'),
    path('partners/', views.ListPartners.as_view(), name='list-partners'),

    # testimonial routes

    path('testimonials/', views.TestimonialList.as_view(), name='testimonials'),
    path('testimonials/<int:pk>/', views.ListTestimonialsById.as_view(), name='list-testimonials-by-id'),
] 
