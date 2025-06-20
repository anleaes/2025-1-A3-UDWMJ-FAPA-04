from django import forms
from .models import Room

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        exclude = ('created_on', 'updated_on')
