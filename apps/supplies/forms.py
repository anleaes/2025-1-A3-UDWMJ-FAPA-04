from django import forms
from .models import Supply

class SupplyForm(forms.ModelForm):

    class Meta:
        model = Supply
        exclude = ('created_on', 'updated_on')