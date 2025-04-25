from django.contrib import admin
from .models import Cartao

admin.site.register(Cartao)  # Exibe de forma mais simples


# @admin.register(Cartao)
# class CartaoAdmin(admin.ModelAdmin):
#     list_display = ('nome_cartao')
#     search_fields = ('nome_cartao')
#     list_filter = ('nome_cartao',)
#     ordering = ('nome_cartao',)
#     fieldsets = (
#         (None, {
#             'fields': ('nome_cartao')
#         }),
#         ('Informações Adicionais', {
#             'fields': ('nome_cartao',),
#             'classes': ('collapse',)
#         }),
#     )
