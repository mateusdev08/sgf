from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.db import transaction
from .models import LancamentoFinanceiro
from plano_contas.models import PlanoContas
from .forms import LancamentoFinanceiroForm


class LancamentoFinanceiroListView(ListView):
    model = LancamentoFinanceiro
    template_name = 'lancamento_financeiro/list.html'
    context_object_name = 'lancamentos'
    paginate_by = 25
    # ordering = ['-data_vencimento']
    ordering = ['-id']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtros para busca
        descricao = self.request.GET.get('descricao')
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')

        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao)

        if data_inicio:
            queryset = queryset.filter(data_vencimento__gte=data_inicio)

        if data_fim:
            queryset = queryset.filter(data_vencimento__lte=data_fim)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicionar informações para filtros
        return context


class LancamentoFinanceiroCreateView(CreateView):
    model = LancamentoFinanceiro
    form_class = LancamentoFinanceiroForm
    template_name = 'lancamento_financeiro/form.html'
    success_url = reverse_lazy('lancamento_financeiro:list')

    @transaction.atomic
    def form_valid(self, form):
        # Não salvar o formulário diretamente, vamos tratar conforme as regras
        lancamento = form.save(commit=False)

        # Obter os objetos e códigos dos campos PlanoContas
        classe_obj = form.cleaned_data['classe']
        grupo_obj = form.cleaned_data['grupo']
        natureza_obj = form.cleaned_data['natureza']

        # Armazenar os códigos explicitamente
        if classe_obj:
            lancamento.cod_classe = classe_obj.cod_classe
        if grupo_obj:
            lancamento.cod_grupo = grupo_obj.cod_grupo
        if natureza_obj:
            lancamento.cod_natureza = natureza_obj.cod_natureza

        # Guardar os objetos relacionados antes de processar
        classe_id = classe_obj.id if classe_obj else None
        grupo_id = grupo_obj.id if grupo_obj else None
        natureza_id = natureza_obj.id if natureza_obj else None

        forma_pagamento = form.cleaned_data['forma_pagamento']
        quantidade_parcela = form.cleaned_data['quantidade_parcela']
        data_vencimento_original = form.cleaned_data['data_vencimento']
        valor_total = form.cleaned_data['valor']

        # Verificar o tipo de forma de pagamento e criar os lançamentos conforme as regras
        tipo_pagamento = forma_pagamento.tipo_pagamento.lower()

        # Caso 1: Pagamento à vista - apenas um lançamento
        if 'vista' in tipo_pagamento:
            lancamento.parcela = 1
            lancamento.save()
            messages.success(
                self.request, 'Lançamento financeiro criado com sucesso!')

        # Caso 2: Pagamento parcelado - múltiplos lançamentos com valores divididos
        elif 'parcelado' in tipo_pagamento and quantidade_parcela > 1:
            valor_parcela = valor_total / quantidade_parcela

            for i in range(quantidade_parcela):
                # Criar um novo lançamento para cada parcela
                novo_lancamento = LancamentoFinanceiro(
                    data_emissao=lancamento.data_emissao,
                    data_vencimento=data_vencimento_original +
                    relativedelta(months=i),
                    classe_id=classe_id,
                    grupo_id=grupo_id,
                    natureza_id=natureza_id,
                    centro_custo=lancamento.centro_custo,
                    movimento_caixa=lancamento.movimento_caixa,
                    conta=lancamento.conta,
                    cartao=lancamento.cartao,
                    operacao=lancamento.operacao,
                    status_movimento=lancamento.status_movimento,
                    forma_pagamento=lancamento.forma_pagamento,
                    quantidade_parcela=quantidade_parcela,
                    parcela=i + 1,  # Número da parcela começando em 1
                    valor=valor_parcela,
                    descricao=lancamento.descricao
                )
                novo_lancamento.save()

            messages.success(
                self.request, f'Lançamento financeiro parcelado em {quantidade_parcela} parcelas criado com sucesso!')

        # Caso 3: Pagamento recorrente - múltiplos lançamentos com mesmo valor
        elif 'recorrente' in tipo_pagamento and quantidade_parcela > 1:
            for i in range(quantidade_parcela):
                # Criar um novo lançamento para cada recorrência
                novo_lancamento = LancamentoFinanceiro(
                    data_emissao=lancamento.data_emissao,
                    data_vencimento=data_vencimento_original +
                    relativedelta(months=i),
                    classe_id=classe_id,
                    grupo_id=grupo_id,
                    natureza_id=natureza_id,
                    centro_custo=lancamento.centro_custo,
                    movimento_caixa=lancamento.movimento_caixa,
                    conta=lancamento.conta,
                    cartao=lancamento.cartao,
                    operacao=lancamento.operacao,
                    status_movimento=lancamento.status_movimento,
                    forma_pagamento=lancamento.forma_pagamento,
                    quantidade_parcela=quantidade_parcela,
                    parcela=i + 1,  # Número da parcela começando em 1
                    valor=valor_total,
                    descricao=lancamento.descricao
                )
                novo_lancamento.save()

            messages.success(
                self.request, f'Lançamento financeiro recorrente criado com sucesso para {quantidade_parcela} meses!')

        # Caso 4: Pagamento repetido - múltiplos lançamentos com mesmo valor e parcela
        elif 'repetir' in tipo_pagamento and quantidade_parcela > 1:
            for i in range(quantidade_parcela):
                # Criar um novo lançamento para cada repetição
                novo_lancamento = LancamentoFinanceiro(
                    data_emissao=lancamento.data_emissao,
                    data_vencimento=data_vencimento_original +
                    relativedelta(months=i),
                    classe_id=classe_id,
                    grupo_id=grupo_id,
                    natureza_id=natureza_id,
                    centro_custo=lancamento.centro_custo,
                    movimento_caixa=lancamento.movimento_caixa,
                    conta=lancamento.conta,
                    cartao=lancamento.cartao,
                    operacao=lancamento.operacao,
                    status_movimento=lancamento.status_movimento,
                    forma_pagamento=lancamento.forma_pagamento,
                    quantidade_parcela=quantidade_parcela,
                    parcela=i + 1,  # Número da parcela começando em 1
                    valor=valor_total,
                    descricao=lancamento.descricao
                )
                novo_lancamento.save()

            messages.success(
                self.request, f'Lançamento financeiro repetido criado com sucesso para {quantidade_parcela} meses!')

        # Caso padrão: qualquer outro tipo de pagamento
        else:
            lancamento.parcela = 1
            lancamento.save()
            messages.success(
                self.request, 'Lançamento financeiro criado com sucesso!')

        return redirect(self.success_url)


class LancamentoFinanceiroUpdateView(UpdateView):
    model = LancamentoFinanceiro
    form_class = LancamentoFinanceiroForm
    template_name = 'lancamento_financeiro/form.html'
    success_url = reverse_lazy('lancamento_financeiro:list')

    def form_valid(self, form):
        # Obter os códigos dos campos PlanoContas antes de salvar
        lancamento = form.save(commit=False)

        # Mantém os IDs dos objetos relacionados enquanto atualiza os dados
        lancamento.save()

        messages.info(
            self.request, 'Lançamento financeiro atualizado com sucesso!')
        return redirect(self.success_url)


class LancamentoFinanceiroDetailView(DetailView):
    model = LancamentoFinanceiro
    template_name = 'lancamento_financeiro/detail.html'
    context_object_name = 'lancamento'


class LancamentoFinanceiroDeleteView(DeleteView):
    model = LancamentoFinanceiro
    template_name = 'lancamento_financeiro/delete.html'
    success_url = reverse_lazy('lancamento_financeiro:list')

    def form_valid(self, form):
        messages.error(
            self.request, 'Lançamento financeiro excluído com sucesso!')
        return super().form_valid(form)
