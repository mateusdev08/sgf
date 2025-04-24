from django.db import models


class CentroCusto(models.Model):
    centro_custo = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Centro Custo'
        verbose_name_plural = 'Centros Custos'

    def __str__(self):
        return self.centro_custo
