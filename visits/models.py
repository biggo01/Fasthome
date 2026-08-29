from django.conf import settings
from django.db import models


class Visit(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "En attente"
        APPROVED = "APPROVED", "Approuvée"
        REJECTED = "REJECTED", "Refusée"
        SCHEDULED = "SCHEDULED", "Programmée"
        COMPLETED = "COMPLETED", "Effectuée"
        CANCELLED = "CANCELLED", "Annulée"

    property = models.ForeignKey(
        "properties.Property",
        on_delete=models.CASCADE,
        related_name="visits",
    )

    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="visit_requests",
    )

    requested_date = models.DateField(
        null=True,
        blank=True,
    )

    requested_time = models.TimeField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    message = models.TextField(
        blank=True,
    )

    agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_visits",
    )

    agent_note = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return (
            f"Visite #{self.pk} - "
            f"{self.property.title}"
        )