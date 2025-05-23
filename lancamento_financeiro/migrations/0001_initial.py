# Generated by Django 5.2 on 2025-05-01 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cartao', '0001_initial'),
        ('centro_custo', '0001_initial'),
        ('conta', '0001_initial'),
        ('forma_pagamento', '0001_initial'),
        ('movimento_caixa', '0001_initial'),
        ('operacao', '0001_initial'),
        ('plano_contas', '0001_initial'),
        ('status_movimento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LancamentoFinanceiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emissao', models.DateTimeField()),
                ('data_vencimento', models.DateTimeField()),
                ('quantidade_parcela', models.IntegerField(default=1)),
                ('parcela', models.IntegerField(default=1)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('cartao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cartao.cartao')),
                ('centro_custo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centro_custo.centrocusto')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lancamentos_classe', to='plano_contas.planocontas')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conta.conta')),
                ('forma_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forma_pagamento.formapagamento')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lancamentos_grupo', to='plano_contas.planocontas')),
                ('movimento_caixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimento_caixa.movimentocaixa')),
                ('natureza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lancamentos_natureza', to='plano_contas.planocontas')),
                ('operacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operacao.operacao')),
                ('status_movimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status_movimento.statusmovimento')),
            ],
            options={
                'verbose_name': 'Lançamento Financeiro',
                'verbose_name_plural': 'Lançamentos Financeiros',
            },
        ),
    ]
