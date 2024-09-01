from django.urls import path
from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
    path('notifications/', views.notifications, name='notifications'),
    path('activity/', views.activity, name='activity'),
    path('security/', views.security, name='security'),
]