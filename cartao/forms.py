from django import forms
from .models import Cartao
from django.core.exceptions import ValidationError


class CartaoForm(forms.ModelForm):
    class Meta:
        model = Cartao
        fields = ['nome_cartao']
        widgets = {
            'nome_cartao': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Para validar se existe uma conta cadastrada no sistema
    def clean(self):
        cleaned_data = super().clean()
        nome_cartao = cleaned_data.get('nome_cartao')

        if nome_cartao:
            if Cartao.objects.filter(
                nome_cartao=nome_cartao
            ).exclude(pk=self.instance.pk if self.instance.pk else None).exists():
                raise ValidationError(
                    'O cartão já está cadastrado no sistema.'
                )

        return cleaned_data
