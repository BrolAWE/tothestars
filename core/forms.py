from django import forms
from django.forms import ModelForm

from core.models import Kite


class KiteForm(ModelForm):
    class Meta:
        model = Kite
        exclude = ('date_subscribed', 'messages_received')
