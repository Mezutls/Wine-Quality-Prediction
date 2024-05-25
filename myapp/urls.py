# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.wine_input_form, name='wine_input_form'),  # Correct view name and pattern
    path('predict/', views.wine_input_form, name='wine_prediction'),  # Updated view name for prediction
]
