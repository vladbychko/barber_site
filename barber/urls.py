from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('services/', views.services_view, name="services"),
    path('booking/', views.booking_view, name="booking"),
]
