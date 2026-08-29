from django import forms

from .models import Visit


class VisitRequestForm(forms.ModelForm):

    class Meta:
        model = Visit

        fields = (
            "requested_date",
            "requested_time",
            "message",
        )

        widgets = {
            "requested_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),

            "requested_time": forms.TimeInput(
                attrs={
                    "type": "time",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": (
                        "Informations complémentaires"
                    ),
                }
            ),
        }