from django.urls import path

from . import views


app_name = "agent_dashboard"


urlpatterns = [
    path(
        "",
        views.dashboard,
        name="dashboard",
    ),
]