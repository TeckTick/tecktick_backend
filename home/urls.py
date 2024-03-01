from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', home, name='home'),
    path('partners/<int:pk>', views.ListPartnersById.as_view(), name='list-partners-by-id'),
    path('partners/update/<int:pk>/', views.UpdatePartners.as_view(), name='update-partner'),
    path('partners/<int:pk>/delete/', views.DeletePartners.as_view(), name='delete-partner'),
    path('partners/new/', views.PostPartners.as_view(), name='create-partner'),
    path('partners/', views.ListPartners.as_view(), name='list-partners'),

    # testimonial routes

    path('testimonials/', views.Testimonials.as_view()),
    path('testimonials/<int:pk>/', views.Testimonial.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
