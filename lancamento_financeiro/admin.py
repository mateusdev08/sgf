from django.contrib import admin
from .models import LancamentoFinanceiro


@admin.register(LancamentoFinanceiro)
class LancamentoFinanceiroAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_vencimento', 'descricao',
                    'valor', 'parcela', 'forma_pagamento')
    list_filter = ('data_vencimento', 'forma_pagamento',
                   'status_movimento', 'operacao')
    search_fields = ('descricao', 'valor')
    date_hierarchy = 'data_vencimento'
    ordering = ('-data_vencimento',)
    fieldsets = (
        (None, {
            'fields': ('data_emissao', 'data_vencimento', 'valor', 'descricao')
        }),
        ('Categorização', {
            'fields': ('classe', 'grupo', 'natureza', 'centro_custo')
        }),
        ('Detalhes do Pagamento', {
            'fields': ('movimento_caixa', 'conta', 'cartao', 'operacao', 'status_movimento', 'forma_pagamento')
        }),
        ('Parcelamento', {
            'fields': ('quantidade_parcela', 'parcela')
        }),
    )
