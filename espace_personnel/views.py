from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from properties.models import Property
from visits.models import Visit


@login_required
def dashboard(request):

    properties_count = Property.objects.filter(
        owner=request.user
    ).count()

    visits_count = Visit.objects.filter(
        requester=request.user
    ).count()

    recent_properties = Property.objects.filter(
        owner=request.user
    )[:5]

    recent_visits = Visit.objects.filter(
        requester=request.user
    ).select_related(
        "property"
    )[:5]

    return render(
        request,
        "espace_personnel/dashboard.html",
        {
            "properties_count": properties_count,
            "visits_count": visits_count,
            "recent_properties": recent_properties,
            "recent_visits": recent_visits,
        },
    )


@login_required
def my_properties(request):

    properties = Property.objects.filter(
        owner=request.user
    )

    return render(
        request,
        "espace_personnel/properties.html",
        {
            "properties": properties,
        },
    )


@login_required
def my_visits(request):

    visits = Visit.objects.filter(
        requester=request.user
    ).select_related(
        "property"
    )

    return render(
        request,
        "espace_personnel/visits.html",
        {
            "visits": visits,
        },
    )