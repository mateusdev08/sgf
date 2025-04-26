from django import forms
from .models import Operacao
from django.core.exceptions import ValidationError


class OperacaoForm(forms.ModelForm):
    class Meta:
        model = Operacao
        fields = ['tipo_operacao']
        widgets = {
            'tipo_operacao': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Para validar se existe uma conta cadastrada no sistema
    def clean(self):
        cleaned_data = super().clean()
        tipo_operacao = cleaned_data.get('tipo_operacao')

        if tipo_operacao:
            if Operacao.objects.filter(
                tipo_operacao=tipo_operacao
            ).exclude(pk=self.instance.pk if self.instance.pk else None).exists():
                raise ValidationError(
                    'O tipo de operação já está cadastrado no sistema.'
                )

        return cleaned_data
