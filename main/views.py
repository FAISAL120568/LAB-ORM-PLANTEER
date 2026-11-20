from django.shortcuts import render
from plants.models import Plant


def home_view(request):
    plants = Plant.objects.order_by("-created_at")[:3]
    return render(request, "main/home.html", {"plants": plants})