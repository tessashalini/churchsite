from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('documents/', views.documents, name='documents'),
    path('finance/', views.finance, name='finance'),
     path("events/", views.events, name="admin-events"),

]

