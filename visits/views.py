from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from properties.models import Property

from .forms import VisitRequestForm
from .models import Visit


@login_required
def request_visit(request, property_id):

    property_obj = get_object_or_404(
        Property,
        pk=property_id,
        status=Property.PublicationStatus.PUBLISHED,
    )

    if request.method == "POST":

        form = VisitRequestForm(
            request.POST
        )

        if form.is_valid():

            visit = form.save(
                commit=False
            )

            visit.property = property_obj
            visit.requester = request.user

            visit.save()

            return redirect(
                "espace_personnel:visits"
            )

    else:
        form = VisitRequestForm()

    return render(
        request,
        "visits/request.html",
        {
            "property": property_obj,
            "form": form,
        },
    )


@login_required
def my_visits(request):

    visits = Visit.objects.filter(
        requester=request.user
    ).select_related(
        "property",
        "agent",
    )

    return render(
        request,
        "visits/list.html",
        {
            "visits": visits,
        },
    )