from django.urls import path
from . import views

urlpatterns = [
    path('picture/<int:pk>/', views.current_datetime, name="picture")
]