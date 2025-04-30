from django import forms
from .models import PlanoContas
from django.core.exceptions import ValidationError


class PlanoContasForm(forms.ModelForm):
    class Meta:
        model = PlanoContas
        fields = ['cod_classe', 'classe', 'cod_grupo', 'grupo', 'cod_natureza', 'natureza']
        widgets = {
            'cod_classe': forms.TextInput(attrs={'class': 'form-control'}),
            'classe': forms.TextInput(attrs={'class': 'form-control'}),
            'cod_grupo': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo': forms.TextInput(attrs={'class': 'form-control'}),
            'cod_natureza': forms.TextInput(attrs={'class': 'form-control'}),
            'natureza': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Para validar se existe uma conta cadastrada no sistema
    def clean(self):
        cleaned_data = super().clean()
        natureza = cleaned_data.get('natureza')

        if natureza:
            if PlanoContas.objects.filter(
                natureza=natureza
            ).exclude(pk=self.instance.pk if self.instance.pk else None).exists():
                raise ValidationError(
                    'Plano de contas já está cadastrado no sistema.'
                )

        return cleaned_data
