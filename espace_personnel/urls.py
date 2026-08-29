from django.urls import path

from . import views


app_name = "espace_personnel"


urlpatterns = [
    path(
        "",
        views.dashboard,
        name="dashboard",
    ),

    path(
        "mes-logements/",
        views.my_properties,
        name="properties",
    ),

    path(
        "mes-visites/",
        views.my_visits,
        name="visits",
    ),
]