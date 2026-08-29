from django.urls import path

from . import views


app_name = "properties"


urlpatterns = [
    path(
        "",
        views.property_list,
        name="list",
    ),

    path(
        "<int:pk>/",
        views.property_detail,
        name="detail",
    ),

    path(
        "publier/",
        views.property_create,
        name="create",
    ),

    path(
        "<int:pk>/modifier/",
        views.property_update,
        name="update",
    ),

    path(
        "<int:pk>/supprimer/",
        views.property_delete,
        name="delete",
    ),
]