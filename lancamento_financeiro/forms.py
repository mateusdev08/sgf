from django import forms
from .models import LancamentoFinanceiro
from plano_contas.models import PlanoContas
from centro_custo.models import CentroCusto
from movimento_caixa.models import MovimentoCaixa
from conta.models import Conta
from cartao.models import Cartao
from operacao.models import Operacao
from status_movimento.models import StatusMovimento
from forma_pagamento.models import FormaPagamento
from django.core.exceptions import ValidationError
import datetime


class ClasseModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        # Retorna apenas o valor da coluna 'classe'
        return obj.classe


class GrupoModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        # Retorna apenas o valor da coluna 'grupo'
        return obj.grupo


class NaturezaModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        # Retorna apenas o valor da coluna 'natureza'
        return obj.natureza


class LancamentoFinanceiroForm(forms.ModelForm):
    # Substituir os campos padrão por campos personalizados
    classe = ClasseModelChoiceField(
        queryset=PlanoContas.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    grupo = GrupoModelChoiceField(
        queryset=PlanoContas.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    natureza = NaturezaModelChoiceField(
        queryset=PlanoContas.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = LancamentoFinanceiro
        fields = [
            'data_emissao', 'data_vencimento', 'classe', 'grupo', 'natureza',
            'centro_custo', 'movimento_caixa', 'conta', 'cartao', 'operacao',
            'status_movimento', 'forma_pagamento', 'quantidade_parcela', 'valor', 'descricao'
        ]
        widgets = {
            'data_emissao': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'data_vencimento': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'centro_custo': forms.Select(attrs={'class': 'form-control'}),
            'movimento_caixa': forms.Select(attrs={'class': 'form-control'}),
            'conta': forms.Select(attrs={'class': 'form-control'}),
            'cartao': forms.Select(attrs={'class': 'form-control'}),
            'operacao': forms.Select(attrs={'class': 'form-control'}),
            'status_movimento': forms.Select(attrs={'class': 'form-control'}),
            'forma_pagamento': forms.Select(attrs={'class': 'form-control'}),
            'quantidade_parcela': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar os campos de plano de contas
        self.fields['classe'].queryset = PlanoContas.objects.exclude(
            classe__isnull=True).exclude(classe='').order_by('classe')

        self.fields['grupo'].queryset = PlanoContas.objects.exclude(
            grupo__isnull=True).exclude(grupo='').order_by('grupo')

        self.fields['natureza'].queryset = PlanoContas.objects.exclude(
            natureza__isnull=True).exclude(natureza='').order_by('natureza')

        # Definir valores iniciais se o objeto existir
        if self.instance and self.instance.pk:
            if self.instance.classe:
                self.fields['classe'].initial = self.instance.classe
            if self.instance.grupo:
                self.fields['grupo'].initial = self.instance.grupo
            if self.instance.natureza:
                self.fields['natureza'].initial = self.instance.natureza

        # Dependendo do tipo de pagamento, pode ou não precisar do cartão
        self.fields['cartao'].required = False

    def clean(self):
        cleaned_data = super().clean()
        forma_pagamento = cleaned_data.get('forma_pagamento')
        quantidade_parcela = cleaned_data.get('quantidade_parcela')

        # Validar quantidade de parcelas
        if quantidade_parcela is not None and quantidade_parcela < 1:
            raise ValidationError(
                "A quantidade de parcelas deve ser maior que zero.")

        # Verificar se cartão é obrigatório para certas formas de pagamento
        if forma_pagamento and 'cartão' in forma_pagamento.tipo_pagamento.lower() and not cleaned_data.get('cartao'):
            self.add_error(
                'cartao', 'Cartão é obrigatório para esta forma de pagamento.')

        return cleaned_data
