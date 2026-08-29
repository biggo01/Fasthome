from django import forms

from .models import Property


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property

        exclude = (
            "owner",
            "status",
            "published_at",
        )

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                }
            ),

            "monthly_price": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "latitude": forms.NumberInput(
                attrs={
                    "step": "0.0000001",
                }
            ),

            "longitude": forms.NumberInput(
                attrs={
                    "step": "0.0000001",
                }
            ),
        }