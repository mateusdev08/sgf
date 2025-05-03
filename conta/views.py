from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .models import Conta
from .forms import ContaForm


class ContaListView(ListView):
    model = Conta
    template_name = 'conta/list.html'
    context_object_name = 'contas'  # Primeira palavra no plural
    paginate_by = 10  # Número de itens por página - Paginação
    ordering = ['id']  # Ordenação padrão - Paginação

    # Início do filtro tipo texto
    def get_queryset(self):
        queryset = super().get_queryset()
        conta = self.request.GET.get('conta')

        if conta and conta.strip():  # Verifica se não está vazio
            try:
                conta = int(conta)  # Converte para inteiro
                queryset = queryset.filter(id=conta)
            except ValueError:
                pass  # Se não conseguir converter para inteiro, ignora o filtro

        return queryset
    # Final do filtro

    # Início da coleta dos dados para o select
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conta'] = Conta.objects.all()
        return context
    # Final


class ContaCreateView(CreateView):
    model = Conta
    form_class = ContaForm
    template_name = 'conta/form.html'
    success_url = reverse_lazy('conta:list')

    # Início da mensagem de sucesso
    def form_valid(self, form):
        messages.success(self.request, 'Conta cadastrada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de sucesso


class ContaUpdateView(UpdateView):
    model = Conta
    form_class = ContaForm
    template_name = 'conta/form.html'
    success_url = reverse_lazy('conta:list')

    # Início da mensagem de alteração
    def form_valid(self, form):
        messages.info(self.request, 'Alteração realizada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de alteração


class ContaDetailView(DetailView):
    model = Conta
    template_name = 'conta/detail.html'
    context_object_name = 'conta'  # Primeira palavra no singular


class ContaDeleteView(DeleteView):
    model = Conta
    template_name = 'conta/delete.html'
    success_url = reverse_lazy('conta:list')

    # Início da mensagem de exclusão
    def form_valid(self, form):
        messages.error(self.request, 'Conta deletada com sucesso!')
        return super().form_valid(form)
    # Final da mensagem de exclusão
