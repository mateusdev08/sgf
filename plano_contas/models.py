from django.db import models


class PlanoContas(models.Model):
    cod_classe = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    cod_grupo = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)
    cod_natureza = models.CharField(max_length=100)
    natureza = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Plano Conta'
        verbose_name_plural = 'Planos Contas'

    def __str__(self):
        return self.natureza
