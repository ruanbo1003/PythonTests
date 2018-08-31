
from django import forms
from django.core.validators import validate_email
from django.shortcuts import get_object_or_404

from irm.company.models import Company


class MultiEmailField(forms.Field):
    def to_python(self, value):
        value = super().to_python(value)
        return value if value else []

    def validate(self, value):
        super().validate(value)

        for email in value:
            validate_email(email)


class InviteForm(forms.Form):
    company_uuid = forms.UUIDField(required=True)
    emails = MultiEmailField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        get_object_or_404(Company, uuid=cleaned_data.get('company_uuid'))
        return cleaned_data


def post(request):
    invite_form = InviteForm(request.data)

    if not invite_form.is_valid():
        print("not valid data")
