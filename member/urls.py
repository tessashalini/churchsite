from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='member_home'),
    path('event/', views.events, name='member_events'),
    path('donate/', views.donate, name='member_donate'),
    path('gallery/', views.gallery, name='member_gallery'),
    path('community/', views.community, name='community'),
    path('thank_you/', views.thank_you, name='thank_you'), 
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('simple_logout/', views.simple_logout, name='simple_logout'),
    path('switch_roles/', views.switch_roles, name='switch_roles'),
    path('api/booked-events/', views.booked_events_api, name='booked_events_api'),
    path('admin_login/', views.admin_login, name='admin_login'),


]


