from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from visits.models import Visit


@staff_member_required
def dashboard(request):

    pending_visits = Visit.objects.filter(
        status=Visit.Status.PENDING
    ).select_related(
        "property",
        "requester",
    )

    return render(
        request,
        "agent_dashboard/dashboard.html",
        {
            "pending_visits": pending_visits,
        },
    )