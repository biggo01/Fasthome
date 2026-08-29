from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)

from .models import User


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User

        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
            "password1",
            "password2",
        )

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Prénom",
                    "autocomplete": "given-name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Nom",
                    "autocomplete": "family-name",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Nom d'utilisateur",
                    "autocomplete": "username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Adresse e-mail",
                    "autocomplete": "email",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Téléphone",
                    "autocomplete": "tel",
                }
            ),
        }


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom d'utilisateur",
                "autocomplete": "username",
            }
        ),
    )

    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Mot de passe",
                "autocomplete": "current-password",
            }
        ),
    )