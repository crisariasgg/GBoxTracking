"""Circles URLs."""

# Django
from django.urls import path


# Views
from .views.contacts import *

urlpatterns = [
    path('index',ContactView.as_view(),name="contact"),    
]