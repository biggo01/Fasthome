from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Compte unique Fasthome.

    Un même utilisateur peut :
    - rechercher un logement ;
    - publier un logement ;
    - demander des visites ;
    - gérer ses propres publications.

    Les agents et administrateurs disposent de permissions
    supplémentaires via is_staff / is_superuser.
    """

    phone = models.CharField(
        max_length=30,
        blank=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    is_phone_verified = models.BooleanField(
        default=False,
    )

    is_profile_completed = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()

        return self.username

    @property
    def is_agent(self):
        return self.is_staff and not self.is_superuser

    @property
    def is_admin(self):
        return self.is_superuser