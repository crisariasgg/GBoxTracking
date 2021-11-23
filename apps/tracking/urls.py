"""Circles URLs."""

# Django
from django.urls import path


# Views
from .views.tracking import *

urlpatterns = [
    path('tracking-search/',TrackingSearchView.as_view(),name="tracking_search"),    
]