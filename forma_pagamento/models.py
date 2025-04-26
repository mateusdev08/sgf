from django.db import models


class FormaPagamento(models.Model):
    tipo_pagamento = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Forma Pagamento'
        verbose_name_plural = 'Formas Pagamentos'

    def __str__(self):
        return self.tipo_pagamento
