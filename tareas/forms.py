from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion',  'importante']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows':3}),
        }
