from django.urls import path
from .views import predict_glucose_view, list_glucose_readings_view, glucose_levels_only_view 

urlpatterns = [
    path('predict/', predict_glucose_view, name='predict'),
    path('readings/', list_glucose_readings_view, name='readings'),
    path('glucose-levels/', glucose_levels_only_view, name='glucose_levels_only'),
]
