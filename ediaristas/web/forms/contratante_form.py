from django import forms
from ..models import Contratante

class ContratanteForm(forms.ModelForm):
    class Meta:
        model = Contratante
        fields = '__all__'