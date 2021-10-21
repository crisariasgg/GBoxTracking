"""Contacts URLs."""

# Django
from django.urls import path


# Views
from .views.contacts import *

urlpatterns = [
    path('contact/',ContactView.as_view(),name="contact"),    
]