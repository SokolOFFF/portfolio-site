from django.urls import path
from .views import home, projects, contacts

urlpatterns = [
    path('', home),
    path('projects', projects),
    path('contacts', contacts)
]