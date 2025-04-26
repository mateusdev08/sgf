from django.db import models


class StatusMovimento(models.Model):
    tipo_status = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Status Movimento'
        verbose_name_plural = 'Status Movimentos'

    def __str__(self):
        return self.tipo_status
