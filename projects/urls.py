from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    # path('project/<int:pk>/', views.project, name='project'),
    # path('project/new/', views.project_new, name='project_new'),
    # path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),
    # path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
    # path('project/<int:pk>/add/', views.project_add, name='project_add'),
    # path('project/<int:pk>/remove/', views.project_remove, name='project_remove'),
]
