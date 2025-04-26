from django.contrib import admin
from .models import Operacao

admin.site.register(Operacao)  # Exibe de forma mais simples


# @admin.register(Operacao)
# class OperacaoAdmin(admin.ModelAdmin):
#     list_display = ('tipo_operacao')
#     search_fields = ('tipo_operacao')
#     list_filter = ('tipo_operacao',)
#     ordering = ('tipo_operacao',)
#     fieldsets = (
#         (None, {
#             'fields': ('tipo_operacao')
#         }),
#         ('Informações Adicionais', {
#             'fields': ('tipo_operacao',),
#             'classes': ('collapse',)
#         }),
#     )
