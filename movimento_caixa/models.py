from django.db import models


class MovimentoCaixa(models.Model):
    tipo_movimento = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Movimento Caixa'
        verbose_name_plural = 'Movimentos Caixas'

    def __str__(self):
        return self.tipo_movimento
