from django.urls import path
from . import views

urlpatterns = [
    path('picture/<int:pk>/', views.current_datetime, name="picture"),
    path('your-name/', views.get_name, name="your_name"),
    path('contact-us/', views.contact_form, name="contact_us"),
]
