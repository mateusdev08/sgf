from django.contrib import admin
from .models import PlanoContas

admin.site.register(PlanoContas)  # Exibe de forma mais simples


# @admin.register(PlanoContas)
# class PlanoContasAdmin(admin.ModelAdmin):
#     list_display = ('natureza')
#     search_fields = ('natureza')
#     list_filter = ('natureza',)
#     ordering = ('natureza',)
#     fieldsets = (
#         (None, {
#             'fields': ('natureza')
#         }),
#         ('Informações Adicionais', {
#             'fields': ('natureza',),
#             'classes': ('collapse',)
#         }),
#     )
