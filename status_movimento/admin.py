from django.contrib import admin
from .models import StatusMovimento

admin.site.register(StatusMovimento)  # Exibe de forma mais simples


# @admin.register(StatusMovimento)
# class StatusMovimentoAdmin(admin.ModelAdmin):
#     list_display = ('tipo_status')
#     search_fields = ('tipo_status')
#     list_filter = ('tipo_status',)
#     ordering = ('tipo_status',)
#     fieldsets = (
#         (None, {
#             'fields': ('tipo_status')
#         }),
#         ('Informações Adicionais', {
#             'fields': ('tipo_status',),
#             'classes': ('collapse',)
#         }),
#     )
