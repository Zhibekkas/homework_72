from django import forms
from webapp.models import Citation


class CitationForm(forms.ModelForm):
    class Meta:
        model = Citation
        fields = ["text", "name", "email_address"]
