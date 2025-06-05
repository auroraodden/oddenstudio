from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('education/', views.education_view, name='education'),
    path('experience/', views.experience_view, name='experience'),
    path('projects/', views.project_view, name='projects'),
    path('skills/', views.skill_view, name='skills'),
    path('contact/', views.contact_view, name='contact'),
]
