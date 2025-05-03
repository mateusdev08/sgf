from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .models import FormaPagamento
from .forms import FormaPagamentoForm


class FormaPagamentoListView(ListView):
    model = FormaPagamento
    template_name = 'forma_pagamento/list.html'
    context_object_name = 'formas'  # Primeira palavra no plural
    paginate_by = 10  # Número de itens por página - Paginação
    ordering = ['id']  # Ordenação padrão - Paginação

    # Início do filtro tipo texto
    def get_queryset(self):
        queryset = super().get_queryset()
        tipo_pagamento = self.request.GET.get('tipo_pagamento')

        if tipo_pagamento and tipo_pagamento.strip():  # Verifica se não está vazio
            try:
                tipo_pagamento = int(tipo_pagamento)  # Converte para inteiro
                queryset = queryset.filter(id=tipo_pagamento)
            except ValueError:
                pass  # Se não conseguir converter para inteiro, ignora o filtro

        return queryset
    # Final do filtro

    # Início da coleta dos dados para o select
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_pagamento'] = FormaPagamento.objects.all()
        return context
    # Final


class FormaPagamentoCreateView(CreateView):
    model = FormaPagamento
    form_class = FormaPagamentoForm
    template_name = 'forma_pagamento/form.html'
    success_url = reverse_lazy('forma_pagamento:list')

    # Início da mensagem de sucesso
    def form_valid(self, form):
        messages.success(
            self.request, 'Forma de pagamento cadastrada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de sucesso


class FormaPagamentoUpdateView(UpdateView):
    model = FormaPagamento
    form_class = FormaPagamentoForm
    template_name = 'forma_pagamento/form.html'
    success_url = reverse_lazy('forma_pagamento:list')

    # Início da mensagem de alteração
    def form_valid(self, form):
        messages.info(self.request, 'Alteração realizada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de alteração


class FormaPagamentoDetailView(DetailView):
    model = FormaPagamento
    template_name = 'forma_pagamento/detail.html'
    context_object_name = 'forma'  # Primeira palavra no singular


class FormaPagamentoDeleteView(DeleteView):
    model = FormaPagamento
    template_name = 'forma_pagamento/delete.html'
    success_url = reverse_lazy('forma_pagamento:list')

    # Início da mensagem de exclusão
    def form_valid(self, form):
        messages.error(self.request, 'Tipo de pagamento deletado com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de exclusão
