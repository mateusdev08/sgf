from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .models import Operacao
from .forms import OperacaoForm


class OperacaoListView(ListView):
    model = Operacao
    template_name = 'operacao/list.html'
    context_object_name = 'operacoes'  # Primeira palavra no plural
    paginate_by = 10  # Número de itens por página - Paginação
    ordering = ['id']  # Ordenação padrão - Paginação

    # Início do filtro tipo texto
    def get_queryset(self):
        queryset = super().get_queryset()
        tipo_operacao = self.request.GET.get('tipo_operacao')

        if tipo_operacao and tipo_operacao.strip():  # Verifica se não está vazio
            try:
                tipo_operacao = int(tipo_operacao)  # Converte para inteiro
                queryset = queryset.filter(id=tipo_operacao)
            except ValueError:
                pass  # Se não conseguir converter para inteiro, ignora o filtro

        return queryset
    # Final do filtro

    # Início da coleta dos dados para o select
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_operacao'] = Operacao.objects.all()
        return context
    # Final


class OperacaoCreateView(CreateView):
    model = Operacao
    form_class = OperacaoForm
    template_name = 'operacao/form.html'
    success_url = reverse_lazy('operacao:list')

    # Início da mensagem de sucesso
    def form_valid(self, form):
        messages.success(
            self.request, 'Tipo de operação cadastrada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de sucesso


class OperacaoUpdateView(UpdateView):
    model = Operacao
    form_class = OperacaoForm
    template_name = 'operacao/form.html'
    success_url = reverse_lazy('operacao:list')

    # Início da mensagem de alteração
    def form_valid(self, form):
        messages.info(self.request, 'Alteração realizada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de alteração


class OperacaoDetailView(DetailView):
    model = Operacao
    template_name = 'operacao/detail.html'
    context_object_name = 'operacao'  # Primeira palavra no singular


class OperacaoDeleteView(DeleteView):
    model = Operacao
    template_name = 'operacao/delete.html'
    success_url = reverse_lazy('operacao:list')

    # Início da mensagem de exclusão
    def form_valid(self, form):
        messages.error(self.request, 'Tipo de operação deletada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de exclusão
