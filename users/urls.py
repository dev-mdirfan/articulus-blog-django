from django.urls import path
from . import views

urlpatterns = [
    path('user-details/<int:pk>/', views.user_details, name='user_details'),
]