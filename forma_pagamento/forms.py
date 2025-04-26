from django import forms
from .models import FormaPagamento
from django.core.exceptions import ValidationError


class FormaPagamentoForm(forms.ModelForm):
    class Meta:
        model = FormaPagamento
        fields = ['tipo_pagamento']
        widgets = {
            'tipo_pagamento': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Para validar se existe uma conta cadastrada no sistema
    def clean(self):
        cleaned_data = super().clean()
        tipo_pagamento = cleaned_data.get('tipo_pagamento')

        if tipo_pagamento:
            if FormaPagamento.objects.filter(
                tipo_pagamento=tipo_pagamento
            ).exclude(pk=self.instance.pk if self.instance.pk else None).exists():
                raise ValidationError(
                    'O tipo de pagamento já está cadastrado no sistema.'
                )

        return cleaned_data
