from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .models import MovimentoCaixa
from .forms import MovimentoCaixaForm


class MovimentoCaixaListView(ListView):
    model = MovimentoCaixa
    template_name = 'movimento_caixa/list.html'
    context_object_name = 'movimentos'  # Primeira palavra no plural
    paginate_by = 10  # Número de itens por página - Paginação
    ordering = ['tipo_movimento']  # Ordenação padrão - Paginação

    # Início do filtro tipo texto
    def get_queryset(self):
        queryset = super().get_queryset()
        tipo_movimento = self.request.GET.get('tipo_movimento')

        if tipo_movimento and tipo_movimento.strip():  # Verifica se não está vazio
            try:
                tipo_movimento = int(tipo_movimento)  # Converte para inteiro
                queryset = queryset.filter(id=tipo_movimento)
            except ValueError:
                pass  # Se não conseguir converter para inteiro, ignora o filtro

        return queryset
    # Final do filtro

    # Início da coleta dos dados para o select
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_movimento'] = MovimentoCaixa.objects.all()
        return context
    # Final


class MovimentoCaixaCreateView(CreateView):
    model = MovimentoCaixa
    form_class = MovimentoCaixaForm
    template_name = 'movimento_caixa/form.html'
    success_url = reverse_lazy('movimento_caixa:list')

    # Início da mensagem de sucesso
    def form_valid(self, form):
        messages.success(self.request, 'Tipo de Movimento cadastrado com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de sucesso


class MovimentoCaixaUpdateView(UpdateView):
    model = MovimentoCaixa
    form_class = MovimentoCaixaForm
    template_name = 'movimento_caixa/form.html'
    success_url = reverse_lazy('movimento_caixa:list')

    # Início da mensagem de alteração
    def form_valid(self, form):
        messages.info(self.request, 'Alteração realizada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de alteração


class MovimentoCaixaDetailView(DetailView):
    model = MovimentoCaixa
    template_name = 'movimento_caixa/detail.html'
    context_object_name = 'movimento'  # Primeira palavra no singular


class MovimentoCaixaDeleteView(DeleteView):
    model = MovimentoCaixa
    template_name = 'movimento_caixa/delete.html'
    success_url = reverse_lazy('movimento_caixa:list')

    # Início da mensagem de exclusão
    def form_valid(self, form):
        messages.error(self.request, 'Tipo de movimento deletado com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de exclusão
