from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Administration Django
    path("admin/", admin.site.urls),

    # Site public
    path("", include("public.urls")),

    # Comptes
    path("compte/", include("accounts.urls")),

    # Logements
    path("logements/", include("properties.urls")),

    # Visites
    path("visites/", include("visits.urls")),

    # Espace personnel
    path("espace/", include("espace_personnel.urls")),

    # Agent Fasthome
    path("agent/", include("agent_dashboard.urls")),

    # Administration métier Fasthome
    path("gestion/", include("admin_dashboard.urls")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )