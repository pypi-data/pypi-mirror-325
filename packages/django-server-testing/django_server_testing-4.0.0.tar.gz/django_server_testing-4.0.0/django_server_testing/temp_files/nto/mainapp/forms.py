from django import forms
from django.core.exceptions import ValidationError

from .models import Template
from .fields import GroupedModelChoiceField, GroupedModelMultipleChoiceField

import itertools


class TemplateForm(forms.ModelForm):
    #files = forms.FileField()
    class Meta:
        model = Template
        fields = "__all__"
        widgets = {
            "phone_number": forms.TextInput(attrs={"type": "tel"}),
        }
        labels = {
            "full_name": "ФИО",
            "phone_number": "Номер телефона",
            "email": "Почта",
        }

    # def clean(self):
    #     cleaned = super().clean()
    #     errors = []
    #     cleaned.get("data") - получение данных "data" из модели
    #
    #     ....
    #
    #     if errors:
    #         raise errors