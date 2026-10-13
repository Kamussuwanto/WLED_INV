
"""
from django.urls import path
from .views import part_list_view

urlpatterns = [
    path('parts/', part_list_view, name='part_list'),
]
"""

from django.urls import path
from .views import inventory_search_view  # Updated import name

urlpatterns = [
    path('parts/', inventory_search_view, name='part_list'), # Updated view function
]
