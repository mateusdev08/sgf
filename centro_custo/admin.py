from django.contrib import admin
from .models import CentroCusto

admin.site.register(CentroCusto)  # Exibe de forma mais simples


# @admin.register(CentroCusto)
# class CentroCustoAdmin(admin.ModelAdmin):
#     list_display = ('centro_custo')
#     search_fields = ('centro_custo')
#     list_filter = ('centro_custo',)
#     ordering = ('centro_custo',)
#     fieldsets = (
#         (None, {
#             'fields': ('centro_custo')
#         }),
#         ('Informações Adicionais', {
#             'fields': ('centro_custo',),
#             'classes': ('collapse',)
#         }),
#     )
