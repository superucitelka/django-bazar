from django.forms import ModelForm
from .models import *

class BazarForm(ModelForm):
    class Meta:
        model = Zbozi
        fields = ['nazev', 'popis', 'cena', 'stav', 'foto', 'druh']

