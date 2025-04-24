from django import forms
from .models import CentroCusto
from django.core.exceptions import ValidationError


class CentroCustoForm(forms.ModelForm):
    class Meta:
        model = CentroCusto
        fields = ['centro_custo']
        widgets = {
            'centro_custo': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Para validar se existe uma conta cadastrada no sistema
    def clean(self):
        cleaned_data = super().clean()
        centro_custo = cleaned_data.get('centro_custo')

        if centro_custo:
            if CentroCusto.objects.filter(
                centro_custo=centro_custo
            ).exclude(pk=self.instance.pk if self.instance.pk else None).exists():
                raise ValidationError(
                    'O centro de custo já está cadastrado no sistema.'
                )

        return cleaned_data
