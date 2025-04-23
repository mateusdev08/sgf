from django.contrib import admin
from .models import MovimentoCaixa

admin.site.register(MovimentoCaixa)  # Exibe de forma mais simples


# @admin.register(MovimentoCaixa)
# class MovimentoCaixaAdmin(admin.ModelAdmin):
#     list_display = ('tipo_movimento')
#     search_fields = ('tipo_movimento')
#     list_filter = ('tipo_movimento',)
#     ordering = ('tipo_movimento',)
#     fieldsets = (
#         (None, {
#             'fields': ('tipo_movimento',)
#         }),
#         ('Informações Adicionais', {
#             'fields': ('tipo_movimento',),
#             'classes': ('collapse',)
#         }),
#     )
