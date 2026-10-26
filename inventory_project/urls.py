

"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # <-- Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    
    # Automatically sends users from http://127.0.0.1:8000/ directly to /parts/
    path('', RedirectView.as_view(url='parts/', permanent=True)), 
]

"""


# inventory_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This automatically sends anyone visiting http://127.0.0.1:8000/ 
    # straight over to http://127.0.0
    path('', RedirectView.as_view(url='parts/', permanent=True)), 
    
    # This handles all your sub-urls like /parts/, /locate/part/X/, etc.
    path('', include('inventory.urls')),
]
