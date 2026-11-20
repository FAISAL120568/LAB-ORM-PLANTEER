from django.shortcuts import render
from .models import Plant


def all_plants_view(request):
    plants = Plant.objects.order_by("-created_at")

    category = request.GET.get("category")
    edible = request.GET.get("edible")

    if category:
        plants = plants.filter(category=category)

    if edible == "yes":
        plants = plants.filter(is_edible=True)
    elif edible == "no":
        plants = plants.filter(is_edible=False)

    context = {
        "plants": plants,
        "categories": Plant.Category.choices,
        "selected_category": category,
        "selected_edible": edible,
    }
    return render(request, "plants/all_plants.html", context)