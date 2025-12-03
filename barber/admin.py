from django.contrib import admin
from .models import Service, Stylist, Booking


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(Stylist)
class StylistAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "experience_years")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "service", "date", "time", "created_at")
    list_filter = ("date", "service")
