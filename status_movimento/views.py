from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .models import StatusMovimento
from .forms import StatusMovimentoForm


class StatusMovimentoListView(ListView):
    model = StatusMovimento
    template_name = 'status_movimento/list.html'
    context_object_name = 'movimentos'  # Primeira palavra no plural
    paginate_by = 10  # Número de itens por página - Paginação
    ordering = ['id']  # Ordenação padrão - Paginação

    # Início do filtro tipo texto
    def get_queryset(self):
        queryset = super().get_queryset()
        tipo_status = self.request.GET.get('tipo_status')

        if tipo_status and tipo_status.strip():  # Verifica se não está vazio
            try:
                tipo_status = int(tipo_status)  # Converte para inteiro
                queryset = queryset.filter(id=tipo_status)
            except ValueError:
                pass  # Se não conseguir converter para inteiro, ignora o filtro

        return queryset
    # Final do filtro

    # Início da coleta dos dados para o select
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_status'] = StatusMovimento.objects.all()
        return context
    # Final


class StatusMovimentoCreateView(CreateView):
    model = StatusMovimento
    form_class = StatusMovimentoForm
    template_name = 'status_movimento/form.html'
    success_url = reverse_lazy('status_movimento:list')

    # Início da mensagem de sucesso
    def form_valid(self, form):
        messages.success(
            self.request, 'Tipo de status cadastrado com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de sucesso


class StatusMovimentoUpdateView(UpdateView):
    model = StatusMovimento
    form_class = StatusMovimentoForm
    template_name = 'status_movimento/form.html'
    success_url = reverse_lazy('status_movimento:list')

    # Início da mensagem de alteração
    def form_valid(self, form):
        messages.info(self.request, 'Alteração realizada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de alteração


class StatusMovimentoDetailView(DetailView):
    model = StatusMovimento
    template_name = 'status_movimento/detail.html'
    context_object_name = 'movimento'  # Primeira palavra no singular


class StatusMovimentoDeleteView(DeleteView):
    model = StatusMovimento
    template_name = 'status_movimento/delete.html'
    success_url = reverse_lazy('status_movimento:list')

    # Início da mensagem de exclusão
    def form_valid(self, form):
        messages.error(self.request, 'Tipo de status deletado com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de exclusão
