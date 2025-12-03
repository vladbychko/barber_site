from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Service, Stylist
from .forms import BookingForm


def index(request):
    services = Service.objects.all()[:3]
    stylists = Stylist.objects.all()[:3]
    return render(request, "barber/index.html", {
        "services": services,
        "stylists": stylists,
    })


def services_view(request):
    services = Service.objects.all()
    return render(request, "barber/services.html", {"services": services})


def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Дякуємо! Ми зателефонуємо, щоб підтвердити візит.")
            return redirect("booking")
    else:
        form = BookingForm()
    return render(request, "barber/booking.html", {"form": form})
