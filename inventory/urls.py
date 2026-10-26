"""

from django.urls import path
from .views import inventory_search_view  # Updated import name
from . import views



urlpatterns = [
    path('', views.inventory_search_view, name='part_list_root'),

    # ... keep your existing dashboard or detail views here ...
    path('parts/', inventory_search_view, name='part_list'), # Updated view function
    path('locate/part/<int:pk>/', views.locate_part, name='locate_part'),
    path('locate/tool/<int:pk>/', views.locate_tool, name='locate_tool'),
]

"""

# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Keep this matching /parts/ exactly as you had it originally
    path('parts/', views.inventory_search_view, name='part_list'),
    
    path('locate/part/<int:pk>/', views.locate_part, name='locate_part'),
    path('locate/tool/<int:pk>/', views.locate_tool, name='locate_tool'),
]


