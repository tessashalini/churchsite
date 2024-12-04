from django.urls import path
from . import views
from member.views import request_event

urlpatterns = [
    path('', views.home, name='member_home'),
    path('event/', views.events, name='member_events'),
    path('donate/', views.donate, name='member_donate'),
    path('gallery/', views.gallery, name='member_gallery'),
    path('get-events/', views.get_events, name='get_events'),
     path('events/request/', request_event, name='request_event'), 
]


