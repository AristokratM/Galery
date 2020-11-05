from django.urls import path
from . import views

urlpatterns = [
    path('picture/<int:pk>/', views.get_picture, name="picture"),
    path('your-name/', views.get_name, name="your-name"),
    path('contact-us/', views.contact_form, name="contact_us"),
    path('pictures/', views.pictures, name="pictures"),
    path('current-date/', views.current_datetime, name="current-date"),
]
