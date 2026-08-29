from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PropertyForm
from .models import Property


def property_list(request):

    properties = Property.objects.filter(
        status=Property.PublicationStatus.PUBLISHED
    ).select_related("owner")

    city = request.GET.get("city")
    property_type = request.GET.get("property_type")

    if city:
        properties = properties.filter(
            city__icontains=city
        )

    if property_type:
        properties = properties.filter(
            property_type=property_type
        )

    return render(
        request,
        "properties/list.html",
        {
            "properties": properties,
        },
    )


def property_detail(request, pk):

    property_obj = get_object_or_404(
        Property.objects.select_related("owner"),
        pk=pk,
    )

    return render(
        request,
        "properties/detail.html",
        {
            "property": property_obj,
        },
    )


@login_required
def property_create(request):

    if request.method == "POST":
        form = PropertyForm(request.POST)

        if form.is_valid():
            property_obj = form.save(
                commit=False
            )

            property_obj.owner = request.user
            property_obj.status = (
                Property.PublicationStatus.PENDING
            )

            property_obj.save()

            return redirect(
                "espace_personnel:properties"
            )
    else:
        form = PropertyForm()

    return render(
        request,
        "properties/create.html",
        {
            "form": form,
        },
    )


@login_required
def property_update(request, pk):

    property_obj = get_object_or_404(
        Property,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        form = PropertyForm(
            request.POST,
            instance=property_obj,
        )

        if form.is_valid():
            property_obj = form.save(
                commit=False
            )

            property_obj.status = (
                Property.PublicationStatus.PENDING
            )

            property_obj.save()

            return redirect(
                "espace_personnel:properties"
            )

    else:
        form = PropertyForm(
            instance=property_obj
        )

    return render(
        request,
        "properties/create.html",
        {
            "form": form,
            "property": property_obj,
        },
    )


@login_required
def property_delete(request, pk):

    property_obj = get_object_or_404(
        Property,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        property_obj.delete()

        return redirect(
            "espace_personnel:properties"
        )

    return render(
        request,
        "properties/delete.html",
        {
            "property": property_obj,
        },
    )