from django.contrib import admin
from .models import FormaPagamento

admin.site.register(FormaPagamento)  # Exibe de forma mais simples


# @admin.register(FormaPagamento)
# class FormaPagamentoAdmin(admin.ModelAdmin):
#     list_display = ('tipo_pagamento')
#     search_fields = ('tipo_pagamento')
#     list_filter = ('tipo_pagamento',)
#     ordering = ('tipo_pagamento',)
#     fieldsets = (
#         (None, {
#             'fields': ('tipo_pagamento')
#         }),
#         ('Informações Adicionais', {
#             'fields': ('tipo_pagamento',),
#             'classes': ('collapse',)
#         }),
#     )
