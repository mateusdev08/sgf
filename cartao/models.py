from django.db import models


class Cartao(models.Model):
    nome_cartao = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cartao'
        verbose_name_plural = 'Cartoes'

    def __str__(self):
        return self.nome_cartao
