from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from accounts.models import User
from properties.models import Property
from visits.models import Visit


@staff_member_required
def dashboard(request):

    context = {
        "users_count": User.objects.count(),

        "properties_count": Property.objects.count(),

        "published_properties_count": (
            Property.objects.filter(
                status=Property.PublicationStatus.PUBLISHED
            ).count()
        ),

        "visits_count": Visit.objects.count(),

        "pending_visits_count": (
            Visit.objects.filter(
                status=Visit.Status.PENDING
            ).count()
        ),
    }

    return render(
        request,
        "admin_dashboard/dashboard.html",
        context,
    )