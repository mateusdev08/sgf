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

    class Meta:
        verbose_name = 'Lançamento Financeiro'
        verbose_name_plural = 'Lançamentos Financeiros'

    def __str__(self):
        return f"Lançamento {self.id} - {self.descricao}"
