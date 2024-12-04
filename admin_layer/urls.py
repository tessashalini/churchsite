from django.urls import path
from . import views
from admin_layer.views import events

urlpatterns = [
    path('', views.home, name='home'),
    # path('events/', views.events, name='events'),
    path('documents/', views.documents, name='documents'),
    path('finance/', views.finance, name='finance'),
     path("events/", views.events, name="admin-events"),
    #  path('events/manage/', manage_events, name='manage_events'),
     path("events/", views.events, name="admin-events"),
]

