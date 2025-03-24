from django.urls import path
from .views import control_panel  # Make sure this matches views.py

urlpatterns = [
    path('', control_panel, name='control_panel'),  # This makes /control/ work
]
