from django.urls import path

from . import views


app_name = "visits"


urlpatterns = [
    path(
        "demander/<int:property_id>/",
        views.request_visit,
        name="request",
    ),

    path(
        "mes-visites/",
        views.my_visits,
        name="my_visits",
    ),
]