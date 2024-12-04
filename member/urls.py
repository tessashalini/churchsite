from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='member_home'),
    path('event/', views.events, name='member_events'),
    path('donate/', views.donate, name='member_donate'),
    path('gallery/', views.gallery, name='member_gallery'),
]


