from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Property(models.Model):

    class PropertyType(models.TextChoices):
        HOUSE = "HOUSE", "Maison"
        APARTMENT = "APARTMENT", "Appartement"
        STUDIO = "STUDIO", "Studio"
        ROOM = "ROOM", "Chambre"
        VILLA = "VILLA", "Villa"
        COMMERCIAL = "COMMERCIAL", "Local commercial"
        OTHER = "OTHER", "Autre"

    class PublicationStatus(models.TextChoices):
        DRAFT = "DRAFT", "Brouillon"
        PENDING = "PENDING", "En attente"
        PUBLISHED = "PUBLISHED", "Publié"
        SUSPENDED = "SUSPENDED", "Suspendu"
        ARCHIVED = "ARCHIVED", "Archivé"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="properties",
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    property_type = models.CharField(
        max_length=30,
        choices=PropertyType.choices,
    )

    province = models.CharField(
        max_length=100,
    )

    city = models.CharField(
        max_length=100,
    )

    municipality = models.CharField(
        max_length=100,
        blank=True,
    )

    neighborhood = models.CharField(
        max_length=150,
        blank=True,
    )

    address = models.CharField(
        max_length=255,
        blank=True,
    )

    bedrooms = models.PositiveIntegerField(
        default=0,
    )

    living_rooms = models.PositiveIntegerField(
        default=0,
    )

    kitchens = models.PositiveIntegerField(
        default=1,
    )

    bathrooms = models.PositiveIntegerField(
        default=0,
    )

    toilets = models.PositiveIntegerField(
        default=0,
    )

    floor = models.IntegerField(
        default=0,
    )

    has_water = models.BooleanField(
        default=False,
    )

    has_electricity = models.BooleanField(
        default=False,
    )

    has_security = models.BooleanField(
        default=False,
    )

    has_parking = models.BooleanField(
        default=False,
    )

    furnished = models.BooleanField(
        default=False,
    )

    condition = models.CharField(
        max_length=100,
        blank=True,
    )

    monthly_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[
            MinValueValidator(0)
        ],
    )

    currency = models.CharField(
        max_length=10,
        default="USD",
    )

    status = models.CharField(
        max_length=20,
        choices=PublicationStatus.choices,
        default=PublicationStatus.DRAFT,
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True,
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title