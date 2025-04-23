from django import forms
from .models import MovimentoCaixa
from django.core.exceptions import ValidationError


class MovimentoCaixaForm(forms.ModelForm):
    class Meta:
        model = MovimentoCaixa
        fields = ['tipo_movimento']
        widgets = {
            'tipo_movimento': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Para validar se existe uma conta cadastrada no sistema
    def clean(self):
        cleaned_data = super().clean()
        tipo_movimento = cleaned_data.get('tipo_movimento')

        if tipo_movimento:
            if MovimentoCaixa.objects.filter(
                tipo_movimento=tipo_movimento
            ).exclude(pk=self.instance.pk if self.instance.pk else None).exists():
                raise ValidationError(
                    'O tipo do movimento de caixa já está cadastrada no sistema.'
                )

        return cleaned_data
