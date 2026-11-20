from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path("all/", views.all_plants_view, name="all_plants"),
]