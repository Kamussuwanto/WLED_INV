

"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
"""
from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')), # This routes your app to the base URL
]
