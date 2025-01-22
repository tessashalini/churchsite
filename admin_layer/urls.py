from django.urls import path
from . import views
from .views import approved_events_api
from .views import booked_events_api


urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('documents/', views.documents, name='documents'),
    path('finance/', views.finance, name='finance'),
    path('simple_logout/', views.simple_logout, name='simple_logout'),
    path('api/approved-events/', approved_events_api, name='approved_events_api'),
    path('api/booked-events/', booked_events_api, name='booked_events_api'),

]






