from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('security/', views.security_focus, name='security'),
    path('contact/', views.contact, name='contact'),
    path('api/projects/', views.api_projects, name='api_projects'),
]
