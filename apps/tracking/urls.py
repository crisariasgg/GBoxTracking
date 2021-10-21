"""Circles URLs."""

# Django
from django.urls import path


# Views
from .views.tracking import *

urlpatterns = [
    path('tracking/',TrackingView.as_view(),name="tracking"),    
]