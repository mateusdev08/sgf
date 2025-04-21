from django.contrib import admin
from .models import Conta

# admin.site.register(Conta)  # Exibe de forma mais simples


@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ('conta', 'saldo_inicial', 'descricao')
    search_fields = ('conta', 'descricao')
    list_filter = ('saldo_inicial',)
    ordering = ('conta',)
    fieldsets = (
        (None, {
            'fields': ('conta', 'saldo_inicial')
        }),
        ('Informações Adicionais', {
            'fields': ('descricao',),
            'classes': ('collapse',)
        }),
    )
