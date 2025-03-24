from django.contrib import admin
from django.urls import path, include
from control.views import control_panel  # Import the main control panel view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', control_panel, name='home'),  # This makes / load the control panel
    path('control/', include('control.urls')),  # Make sure /control/ works
]
