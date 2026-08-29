from django.shortcuts import render

from properties.models import Property


def home(request):

    featured_properties = (
        Property.objects
        .filter(
            status=Property.PublicationStatus.PUBLISHED
        )
        .select_related("owner")[:8]
    )

    return render(
        request,
        "public/home.html",
        {
            "featured_properties": featured_properties,
        },
    )