from django.db import models
from plano_contas.models import PlanoContas
from centro_custo.models import CentroCusto
from movimento_caixa.models import MovimentoCaixa
from conta.models import Conta
from cartao.models import Cartao
from operacao.models import Operacao
from status_movimento.models import StatusMovimento
from forma_pagamento.models import FormaPagamento


class LancamentoFinanceiro(models.Model):
    data_emissao = models.DateTimeField()
    data_vencimento = models.DateTimeField()
    classe = models.ForeignKey(
        PlanoContas, on_delete=models.CASCADE, related_name='lancamentos_classe')
    grupo = models.ForeignKey(
        PlanoContas, on_delete=models.CASCADE, related_name='lancamentos_grupo')
    natureza = models.ForeignKey(
        PlanoContas, on_delete=models.CASCADE, related_name='lancamentos_natureza')
    centro_custo = models.ForeignKey(CentroCusto, on_delete=models.CASCADE)
    movimento_caixa = models.ForeignKey(
        MovimentoCaixa, on_delete=models.CASCADE)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    cartao = models.ForeignKey(
        Cartao, on_delete=models.CASCADE, null=True, blank=True)
    operacao = models.ForeignKey(Operacao, on_delete=models.CASCADE)
    status_movimento = models.ForeignKey(
        StatusMovimento, on_delete=models.CASCADE)
    forma_pagamento = models.ForeignKey(
        FormaPagamento, on_delete=models.CASCADE)
    quantidade_parcela = models.IntegerField(default=1)
    parcela = models.IntegerField(default=1)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    # Novos campos para armazenar os códigos
    cod_classe = models.CharField(max_length=100, null=True, blank=True)
    cod_grupo = models.CharField(max_length=100, null=True, blank=True)
    cod_natureza = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Lançamento Financeiro'
        verbose_name_plural = 'Lançamentos Financeiros'

    def __str__(self):
        return f"Lançamento {self.id} - {self.descricao}"

    def save(self, *args, **kwargs):
        # Antes de salvar, vamos garantir que os códigos sejam capturados
        if self.classe and not self.cod_classe:
            self.cod_classe = self.classe.cod_classe
        if self.grupo and not self.cod_grupo:
            self.cod_grupo = self.grupo.cod_grupo
        if self.natureza and not self.cod_natureza:
            self.cod_natureza = self.natureza.cod_natureza

        super().save(*args, **kwargs)
