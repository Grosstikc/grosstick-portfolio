from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),
    path('about/', views.about_view, name='about'),
    path('skills/', views.skills_view, name='skills'),
    path('projects/', views.projects_view, name='projects'),
    path('contact/', views.contact_view, name='contact'),
]
