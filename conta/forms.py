from django import forms
from .models import Conta
from django.core.exceptions import ValidationError


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['conta', 'saldo_inicial', 'descricao']
        widgets = {
            'conta': forms.TextInput(attrs={'class': 'form-control'}),
            'saldo_inicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    # Para validar se existe uma conta cadastrada no sistema
    def clean(self):
        cleaned_data = super().clean()
        conta = cleaned_data.get('conta')
        saldo_inicial = cleaned_data.get('saldo_inicial')
        descricao = cleaned_data.get('descricao')

        if conta and saldo_inicial is not None and descricao:
            if Conta.objects.filter(
                conta=conta
                # conta=conta,
                # saldo_inicial=saldo_inicial,
                # descricao=descricao
            ).exclude(pk=self.instance.pk if self.instance.pk else None).exists():
                raise ValidationError(
                    'Conta já está cadastrada no sistema.'
                )

        return cleaned_data
