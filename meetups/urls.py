
from django.urls import path
from . import views


urlpatterns = [
    path('listing/', views.list, name= 'all-meetups'),  # our-domain.com/meetups
    path('create/', views.create_student),
    path('indexing/',views.index),
    path('detailing/<slug:meetup_slug>', views.meetup_details, name= 'meetup-detail'), # our_domain.com/meetups/<dynamic_path_segment>
    path('<slug:meetup_slug>/success/', views.confirm_registration, name = 'confirm-registration')
]

