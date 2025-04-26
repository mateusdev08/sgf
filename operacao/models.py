from django.db import models


class Operacao(models.Model):
    tipo_operacao = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Operacao'
        verbose_name_plural = 'Operacoes'

    def __str__(self):
        return self.tipo_operacao
